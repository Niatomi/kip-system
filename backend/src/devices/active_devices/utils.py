from fastapi import Depends
from src.auth.oauth2 import get_current_user
from src.models import Users


async def get_user_role(user: Users = Depends(get_current_user)):
    return user.role
