from fastapi import Depends
from src.auth.oauth2 import get_current_user
from src.models import Users

from src.models import Roles
from fastapi.exceptions import HTTPException
from fastapi import status


async def get_user_role(user: Users = Depends(get_current_user)):
    return user.role


async def check_user_is_not_worker(
        role: Roles = Depends(get_user_role)):
    if role == Roles.worker:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                            detail="User don't have permissions")
