from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.responses import JSONResponse

from src.database import get_async_session
from .schemas import *
from sqlalchemy.ext.asyncio import AsyncSession

from . import utils
from src.auth.exceptions import InvalidCredentialsException
from .oauth2 import (
    create_access_token
)
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from .schemas import InvalidCredentialsResponse
from .schemas import UserAlredyExistsResponse

from src.repository.user import (
    UserRepository,
    UserNotFoundException
)
from .service import form_available_resotre_methods

from typing import List

from src.user import schemas as user_schemas

from src.auth.exceptions import UserNeedToReactivateAccountException

router = APIRouter(
    tags=["Authentication"],
    prefix='/auth'
)


@router.post('/sign_in',
             responses={
                 status.HTTP_403_FORBIDDEN: {
                     "model": InvalidCredentialsResponse,
                     "description": "User credentials is invalid"
                 },
                 status.HTTP_200_OK: {
                     "model": UserToken,
                     "description": "Credentials is valid successfully logged in"
                 }
             },
             response_model=UserToken)
async def sign_in(user_credentials: OAuth2PasswordRequestForm = Depends(),
                  session: AsyncSession = Depends(get_async_session)):
    try:
        user_from_db = await UserRepository.get_by_login(session=session,
                                                         login=user_credentials.username)
    except UserNotFoundException:
        raise InvalidCredentialsException
    if user_from_db.deleted_at is not None:
        raise UserNeedToReactivateAccountException
    if not utils.verify(user_credentials.password, user_from_db.password):
        raise InvalidCredentialsException

    user_token = UserToken()
    user_token.access_token = create_access_token({
        "user_id": str(user_from_db.id)})
    return user_token.dict()


@router.post('/sign_up',
             responses={
                 status.HTTP_400_BAD_REQUEST: {
                     "model": UserAlredyExistsResponse,
                     "description": "User already exists"
                 },
                 status.HTTP_201_CREATED: {
                     "model": UserCreatedResponse,
                     "description": "User created"
                 }
             },
             response_model=UserCreatedResponse)
async def sign_up(sign_up_user: UserCredentials,
                  session: AsyncSession = Depends(get_async_session)):
    await UserRepository.create(session=session, user_credentials=sign_up_user)
    response = UserCreatedResponse()
    return JSONResponse(status_code=response.status_code, content=response.dict())
