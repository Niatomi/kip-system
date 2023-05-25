from src.models import Users
from fastapi import status
from fastapi import Depends
from fastapi.exceptions import HTTPException

from fastapi.security import OAuth2PasswordBearer

from jose import JWTError
from jose import jwt

from datetime import (
    datetime,
    timedelta
)

from src.config import (
    auth_config,
    api_config
)


SECRET = auth_config.jwt_secret
ALGORITHM = auth_config.jwt_alg
ACCESS_TOKEN_EXPIRE_MINUTES = auth_config.jwt_exp
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f'{api_config.api_version_path}/auth/sign_in')


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
        token_data = {}
        token_data['user_id'] = id
    except JWTError:
        raise credentials_exception
    return token_data


async def get_current_user(token: str = Depends(oauth2_scheme)) -> Users:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized')
    try:
        token_data = verify_access_token(token, credentials_exception)
    except credentials_exception:
        raise credentials_exception
    user = await Users.filter(id=token_data['user_id']).first()
    return user
