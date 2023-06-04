from fastapi.exceptions import HTTPException
from fastapi import status
from .. import models


async def check_device_is_exists(id):
    if await models.ActiveDevices.filter(id=id).first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Device is not found')


def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month
