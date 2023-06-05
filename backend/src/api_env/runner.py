from .init_users import init_users
from .init_device_pool import add_devices
from .init_active_devices import add_active_devices
from .init_some_records import add_some_records
from sqlalchemy.ext.asyncio import AsyncSession


async def run(session: AsyncSession):
    admin, chief, worker = await init_users()
    devices = await add_devices()
    await add_active_devices(admin, chief, worker, devices, session)
    await add_some_records(admin, chief, worker, devices, session)
