from .oauth2 import verify_access_token
from fastapi.responses import JSONResponse
from .schemas import UserCredentials
from fastapi import status
from fastapi.exceptions import HTTPException
from src.models import Users
from fastapi import APIRouter
from fastapi import Depends
from tortoise.expressions import Q
from . import schemas as auth_schemas

from . import utils
from .oauth2 import (
    create_access_token
)
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .utils import hash

router = APIRouter(
    tags=["Authentication"],
    prefix='/auth'
)


@router.post('/sign_in')
async def sign_in(user_credentials: OAuth2PasswordRequestForm = Depends()):
    user = await Users.filter(username=user_credentials.username).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Login failed')
    if not utils.verify(user_credentials.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Login failed')

    user_token = auth_schemas.UserToken()
    user_token.access_token = create_access_token({
        "user_id": str(user.id)})
    return user_token


@router.post('/sign_up')
async def sign_up(sign_up_user: UserCredentials):
    user = await Users.filter(Q(username=sign_up_user.username) |
                              Q(email=sign_up_user.email)).first()
    if user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User already exists')
    sign_up_user = sign_up_user.dict()
    sign_up_user['password_hash'] = hash(sign_up_user.pop('password'))

    await Users.create(**sign_up_user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=None)


@router.put('/refresh_token')
async def refresh_token(token_schema: auth_schemas.UserToken):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Bad token')

    user_id = verify_access_token(
        token=token_schema.access_token,
        credentials_exception=credentials_exception)
    print(user_id)

    user_token = auth_schemas.UserToken()
    user_token.access_token = create_access_token({
        "user_id": str(user_id)})
    return user_token
