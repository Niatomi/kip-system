from src.devices import models
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta
from datetime import datetime

actions = ['INSTALLED', "CHECKED", "CHECKED", "REPAIRED", "CHECKED"]


async def add_some_records(admin, chief, worker, devices, session: AsyncSession):

    delta = timedelta(days=60)

    for device in devices:
        reg_date = datetime(2020, 1, 1, 0, 0) + delta
        action_delta = timedelta(days=30)
        for action in actions:
            click_object = {
                'id': str(uuid4()),
                'device_id': device['device_info']['id'],
                'responsible_person': worker.id,
                'action': action.upper(),
                'created_by': chief.id,
                'created_at': reg_date + action_delta
            }
            action_delta = timedelta(days=action_delta.days)
            await session.execute(models.Events.__table__.insert(), click_object)
        delta = timedelta(days=delta.days * 2)
