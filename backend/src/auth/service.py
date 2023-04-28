from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.repository.user import UserRepository
from src.user.schemas import (
    TypesOfRestoreMethods,
    AvailableTypesOfRestoreMethods
)

from fastapi import Depends


async def form_available_resotre_methods(login: str,
                                         session: AsyncSession = Depends(get_async_session)):
    user = await UserRepository.get_by_login(session=session, login=login)
    methods = []
    if (user.email is not None) & user.is_email_confirmed:
        methods.append(TypesOfRestoreMethods.EMAIL)
    if user.telegram_id:
        methods.append(TypesOfRestoreMethods.TELEGRAM)
    if user.phone_number:
        methods.append(TypesOfRestoreMethods.PHONE_NUMBER)
    return AvailableTypesOfRestoreMethods(methods=methods)
