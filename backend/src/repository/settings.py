from src.auth.schemas import UserCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from src.user.exceptions import UserNotFoundException

from sqlalchemy import select
from sqlalchemy import delete
from sqlalchemy import update
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import ENUM

from src.user.models import User
from src.auth.exceptions import UserAlreadyExistsException

from src.auth.utils import hash

from src.user.models import User
from src.user.schemas import UserUpdate
from src.user.schemas import UserSecuirityUpdate
from src.user.exceptions import (EmailAlreadyInUseException,
                                 TelegramAlreadyInUseException,
                                 PhoneNumberAlreadyInUseException,
                                 SecuirityUpdateException
                                 )

from datetime import datetime
from src.settings.models import Settings


class Settings():

    # @staticmethod
    # async def create(session: AsyncSession, settings: Settings):
    #     if await UserRepository.__verify_user_is_not_exists(
    #             session=session, user_credentials=user_credentials):
    #         user_credentials.password = hash(user_credentials.password)
    #         uc = User(**user_credentials.dict())
    #         uc.role_id = await get_default_client_role_id_setter(session=session)
    #         session.add(uc)
    #         await session.commit()
