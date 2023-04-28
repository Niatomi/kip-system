from src.user.models import User
from fastapi import Depends
from fastapi import Form

from src.auth.oauth2 import get_current_user
from src.auth.utils import verify

from src.auth.exceptions import InvalidCredentialsException
from src.user.schemas import UserSecuirityUpdate
from src.user.exceptions import SecuirityUpdateException


async def verify_passwords_and_get_user(
        user_current_password: str = Form(),
        current_user: User = Depends(get_current_user)):
    if not verify(user_current_password, current_user.password):
        raise InvalidCredentialsException
    return current_user


async def check_update_schema(secuirity_update_schema: UserSecuirityUpdate = Depends()):
    secuirity_update_schema: dict = secuirity_update_schema.dict()
    for k, v in secuirity_update_schema.copy().items():
        if v is None:
            secuirity_update_schema.pop(k)
    if len(secuirity_update_schema) == 0:
        raise SecuirityUpdateException
    return secuirity_update_schema
