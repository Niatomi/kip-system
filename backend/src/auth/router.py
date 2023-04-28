from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.responses import JSONResponse

from src.database import get_async_session
from . import schemas as auth_schemas
from sqlalchemy.ext.asyncio import AsyncSession

from . import utils
from src.auth.exceptions import InvalidCredentialsException
from .oauth2 import (
    create_access_token
)
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from src.repository.user import (
    UserRepository,
    UserNotFoundException
)

router = APIRouter(
    tags=["Authentication"],
    prefix='/auth'
)


@router.post('/sign_in',
             responses={
                 status.HTTP_403_FORBIDDEN: {
                     "model": auth_schemas.InvalidCredentialsResponse,
                     "description": "User credentials is invalid"
                 },
                 status.HTTP_200_OK: {
                     "model": auth_schemas.UserToken,
                     "description": "Credentials is valid successfully logged in"
                 }
             },
             response_model=auth_schemas.UserToken)
async def sign_in(user_credentials: OAuth2PasswordRequestForm = Depends(),
                  session: AsyncSession = Depends(get_async_session)):
    try:
        user_from_db = await UserRepository.get_by_login(session=session,
                                                         login=user_credentials.username)
    except UserNotFoundException:
        raise InvalidCredentialsException
    if not utils.verify(user_credentials.password, user_from_db.password):
        raise InvalidCredentialsException

    user_token = auth_schemas.UserToken()
    user_token.access_token = create_access_token({
        "user_id": str(user_from_db.id)})
    return user_token.dict()


@router.post('/sign_up',
             responses={
                 status.HTTP_400_BAD_REQUEST: {
                     "model": auth_schemas.UserAlredyExistsResponse,
                     "description": "User already exists"
                 },
                 status.HTTP_201_CREATED: {
                     "model": auth_schemas.UserCreatedResponse,
                     "description": "User created"
                 }
             },
             response_model=auth_schemas.UserCreatedResponse)
async def sign_up(sign_up_user: auth_schemas.UserCredentials,
                  session: AsyncSession = Depends(get_async_session)):
    await UserRepository.create(session=session, user_credentials=sign_up_user)
    response = auth_schemas.UserCreatedResponse()
    return JSONResponse(status_code=response.status_code, content=response.dict())
