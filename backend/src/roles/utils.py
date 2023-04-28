from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from fastapi import Depends

from src.repository.roles import RolesRepository
from src.roles.models import Role


async def get_default_client_role_id_setter(session: AsyncSession = Depends(get_async_session)):
    role_instance: Role = await RolesRepository.get_by_name(session=session, name='CLIENT')
    id = role_instance.id
    return id
