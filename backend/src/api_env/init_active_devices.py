from src.devices import models
from tortoise.transactions import in_transaction
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta
from datetime import datetime


{
    "invent_number": "string",
    "serial_number": "string",
    "place": "string",
    "device_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}


async def add_active_devices(admin, chief, worker, devices, session: AsyncSession):

    delta = timedelta(days=60)
    reg_date = datetime(2020, 1, 1, 0, 0)

    devs = []
    i = -1
    for device in devices:
        i += 1
        append_device = {}
        append_device['device_id'] = device['device_info']['id']
        invent_number = 100 + i
        append_device['invent_number'] = str(invent_number)
        append_device['serial_number'] = '33pkasfvmpef33'
        append_device['place'] = 'Новоградская 7'

        await models.ActiveDevices.create(**append_device)
        de = await models.ActiveDevices.filter(invent_number=append_device['invent_number']).first()
        append_device['device_id'] = de.id

        devs.append(de.id)
        click_object = {
            'id': str(uuid4()),
            'device_id': de.id,
            'responsible_person': worker.id,
            'action': 'REGISTRED',
            'created_at': reg_date + delta,
            'created_by': chief.id
        }
        delta = timedelta(days=delta.days * 2)

        await session.execute(models.Events.__table__.insert(), click_object)
        device['id'] = click_object['device_id']
    return devs
