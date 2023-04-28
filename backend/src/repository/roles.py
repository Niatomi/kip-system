from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import func

from src.roles import schemas
from src.roles.models import Role
from src.roles.exceptions import RoleAlreadyExistsException, RoleNotFoundException

import json


class RolesRepository():

    @staticmethod
    async def __verify_role_not_found(session: AsyncSession, role_name: str):
        query = select(Role).where(Role.role_name == role_name)
        result = await session.execute(query)
        role = result.scalars().first()
        if role is not None:
            raise RoleAlreadyExistsException
        return True

    @staticmethod
    async def create(session: AsyncSession, role_create: schemas.RoleCreate):
        if await RolesRepository.__verify_role_not_found(
                session=session, role_name=role_create.role_name):
            role_create.role_name = role_create.role_name.upper()
            role_create = role_create.dict()
            session.add(Role(role_name=role_create['role_name'],
                             permissions=json.dumps(role_create['access'])))
            await session.commit()

    @staticmethod
    async def update_by_name(session: AsyncSession, role_name: str, role_update: schemas.RoleUpdate):
        role_name = role_name.upper()
        role = await RolesRepository.get_by_name(session=session, name=role_name)
        if role is None:
            raise RoleNotFoundException
        role.role_name.upper()
        role_updated = {}
        role_updated['id'] = role.id
        role_updated['permissions'] = json.dumps(role_update.dict()['access'])

        statement = update(Role).where(Role.id == role.id).values(role_updated)
        await session.execute(statement)
        await session.commit()
        return await RolesRepository.get_by_id(session=session, id=role.id)

    @staticmethod
    async def get_by_id(session: AsyncSession, id: int):
        query = select(Role).where(Role.id == id)
        result = await session.execute(query)
        role = result.scalars().first()

        if role is None:
            raise RoleNotFoundException

        buf_role_obj = Role()
        buf_role_obj.id = role.id
        buf_role_obj.role_name = role.role_name
        buf_role_obj.permissions = json.loads(role.permissions)
        return buf_role_obj

    @staticmethod
    async def get_by_name(session: AsyncSession, name: str):
        name = name.upper()
        query = select(Role).filter(Role.role_name == name)
        result = await session.execute(query)
        role = result.scalars().first()

        if role is None:
            raise RoleNotFoundException

        buf_role_obj = Role()
        buf_role_obj.id = role.id
        buf_role_obj.role_name = role.role_name
        buf_role_obj.permissions = json.loads(role.permissions)
        return buf_role_obj

    @staticmethod
    async def count_roles(session: AsyncSession):
        query = select(func.count(Role.id)).where(Role.permissions is not None)
        result = await session.execute(query)
        count = result.scalars().first()
        return count
