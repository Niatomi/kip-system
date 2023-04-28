from src.auth.schemas import UserCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from src.user.exceptions import UserNotFoundException

from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import func

from src.auth.exceptions import UserAlreadyExistsException

from src.auth.utils import hash

from src.user.models import User
from src.user.schemas import UserUpdate
from src.user.exceptions import (EmailAlreadyInUseException,
                                 TelegramAlreadyInUseException,
                                 PhoneNumberAlreadyInUseException,
                                 )

from datetime import datetime
from src.roles.utils import get_default_client_role_id_setter


class UserRepository():

    @staticmethod
    async def __verify_user_is_not_exists(session: AsyncSession, user_credentials: UserCredentials):
        query = select(User).where(User.email == user_credentials.email)
        result = await session.execute(query)
        user = result.scalars().first()
        if user is not None:
            raise UserAlreadyExistsException

        query = select(User).where(User.username == user_credentials.username)
        result = await session.execute(query)
        user = result.scalars().first()
        if user is not None:
            raise UserAlreadyExistsException

        return True

    @staticmethod
    async def create(session: AsyncSession, user_credentials: UserCredentials) -> User:
        if await UserRepository.__verify_user_is_not_exists(
                session=session, user_credentials=user_credentials):
            user_credentials.password = hash(user_credentials.password)
            uc = User(**user_credentials.dict())
            uc.role_id = await get_default_client_role_id_setter(session=session)
            session.add(uc)
            await session.commit()

    @staticmethod
    async def get_by_id(session: AsyncSession, user_id: UUID) -> User:
        query = select(User).where(User.id == user_id)
        result = await session.execute(query)
        user = result.scalars().first()

        if user is None:
            raise UserNotFoundException
        return user

    @staticmethod
    async def get_by_login(session: AsyncSession, login: str) -> User:
        query = (select(User)
                 .filter(
                     (User.username == login) |
                     (User.phone_number == login) |
            (User.email == login)))
        result = await session.execute(query)
        user = result.scalars().first()

        if user is None:
            raise UserNotFoundException

        return user

    @staticmethod
    async def update_by_id(session: AsyncSession, id: UUID, user_update: UserUpdate) -> User:
        user = await UserRepository.get_by_id(session=session, user_id=id)
        if user is None:
            raise UserNotFoundException
        updated_user = user_update.dict()
        updated_user['id'] = id
        statement = update(User).where(User.id == id).values(updated_user)
        await session.execute(statement)
        await session.commit()
        return await UserRepository.get_by_id(session=session, user_id=id)

    @staticmethod
    async def __form_update_user_security(session: AsyncSession,
                                          updated_user: dict,
                                          param: str,
                                          value: str):
        query = select(func.count(User.id)).filter(
            getattr(User, param).like("%%%s%%" % value)
        )
        result = await session.execute(query)
        if result.scalar() >= 1:
            if param == "phone_number":
                raise PhoneNumberAlreadyInUseException
            if param == "email":
                raise EmailAlreadyInUseException
            if param == "telegram_id":
                raise TelegramAlreadyInUseException

            # ADD SMTP EVENTER
        updated_user['phone_number'] = value
        updated_user[f'is_{param}_confirmed'] = False

        return updated_user

    @staticmethod
    async def secuirity_update(session: AsyncSession,
                               id: UUID, secuirity_update_dict: dict) -> User:
        user = await UserRepository.get_by_id(session=session, user_id=id)
        if user is None:
            raise UserNotFoundException

        updated_user = secuirity_update_dict.copy()
        updated_user.pop('password')
        for k, v in updated_user.copy().items():
            updated_user = (await UserRepository.
                            __form_update_user_security(session=session,
                                                        updated_user=updated_user,
                                                        param=k,
                                                        value=v))

        if secuirity_update_dict.get('password') is not None:
            updated_user['password'] = hash(
                secuirity_update_dict.get('password'))
        updated_user['id'] = id

        statement = update(User).where(User.id == id).values(**updated_user)
        await session.execute(statement)
        await session.commit()
        return await UserRepository.get_by_id(session=session, user_id=id)

    @staticmethod
    async def fake_delete_by_id(session: AsyncSession, id: UUID):
        user_to_delete = await UserRepository.get_by_id(session=session, user_id=id)
        if user_to_delete is None:
            raise UserNotFoundException
        exceptioned_columns = ['id', 'username', 'email', 'password']

        nullify = False
        for col in user_to_delete.__table__._columns.keys():
            for ex in exceptioned_columns:
                if col == ex or col.find('_confirmed') != -1:
                    nullify = False
                    break
                nullify = True
            if nullify:
                setattr(user_to_delete, col, None)

        user_to_delete.deleted_at = datetime.utcnow()
        user_to_delete.is_email_confirmed = True
        await session.commit()
        return await UserRepository.get_by_id(session=session, user_id=id)
