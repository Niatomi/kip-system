from fastapi import Depends
from src.auth.exceptions import InvalidCredentialsException

from fastapi.security import OAuth2PasswordBearer

from . import schemas

from jose import JWTError
from jose import jwt

from uuid import UUID
from datetime import (
    datetime,
    timedelta
)

from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session

from src.config import auth_config
from src.repository.user import UserRepository
from src.user.models import User


SECRET = auth_config.jwt_secret
ALGORITHM = auth_config.jwt_alg
ACCESS_TOKEN_EXPIRE_MINUTES = auth_config.jwt_exp
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='v1/auth/sign_in')


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        id: str = payload.get('user_id')
        if id is None:
            raise credentials_exception
        token_data = schemas.UserToken()
        token_data.access_token = id
    except JWTError:
        raise credentials_exception
    return token_data


async def get_current_user(token: str = Depends(oauth2_scheme),
                           session: AsyncSession = Depends(get_async_session)) -> User:
    credentials_exception = InvalidCredentialsException
    try:
        access_token = verify_access_token(token, credentials_exception)
        user = await UserRepository.get_by_id(session=session,
                                              user_id=UUID(access_token.access_token))
    except InvalidCredentialsException:
        raise credentials_exception
    return user
