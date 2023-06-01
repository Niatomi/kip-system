from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .. import utils
from collections import ChainMap
from tortoise.transactions import in_transaction
from .. import models
from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi import APIRouter
from fastapi import Depends
from src.database import get_session
from src.utils import check_user_is_not_worker
from . import schemas

router = APIRouter(prefix='/devices_in_use',
                   dependencies=[Depends(check_user_is_not_worker)],
                   tags=['Devices In Use'])

# Many devices


@router.get('/')
async def get_devices_by_params_in_pages(
        params: schemas.GetParams = Depends(schemas.GetParams)):
    return 'Not implemented'


@router.get('/categories')
async def get_avaiable_categories():
    device_pool_ids = await models.ActiveDevices.all().distinct().values('device_id')
    if device_pool_ids is None:
        return None

    specifications = []
    mongo_ids = []
    for v in device_pool_ids:
        mongo_device = await models.DevicesPool.filter(id=v['device_id']).first()
        if mongo_ids.count(mongo_device.mongo_id) == 0:
            mongo_ids.append(mongo_device.mongo_id)
            res = await utils.get_mongo_object_by_id(mongo_device.mongo_id)
            specifications.append(res['specifications'])

    specifications = [item for sublist in specifications for item in sublist]
    specifications = dict(ChainMap(*specifications))

    res = set()
    for v in specifications.keys():
        res.add(v)
    res = list(res)
    res.sort()
    return res


@router.get('/reposponsible_persons')
async def get_reponsible_presons():
    return 'Not implemented'


@router.get('/actions')
async def get_status(session: AsyncSession = Depends(get_session)):
    query = select(models.Events.action).distinct(models.Events.action)
    result = await session.execute(query)
    print(result)
    return 'Not implemented'


@router.get('/places')
async def get_places_of_installation():
    places = await models.ActiveDevices.all().distinct().values('place')
    return [p['place'] for p in places]

# One devices


@router.post('/')
async def add_device(device: models.ActiveDevicesPydanticPost):
    async with in_transaction():
        model = await models.ActiveDevices.create(**device.dict())
    return model


@router.put('/device/{id}')
async def update_device(id: str, device: models.ActiveDevicesPydanticPost):
    if await models.ActiveDevices.filter(id=id).first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Device is not found')

    async with in_transaction():
        await models.ActiveDevices.filter(id=id).update(**device.dict())
    return await models.ActiveDevices.filter(id=id).first()


@router.get('/device/{id}', response_model=models.ActiveDevicesPydanticGet)
async def get_device(id: str):
    return await models.ActiveDevices.filter(id=id).prefetch_related('device').first()


@router.get('/device/{id}/ammortization')
async def calc_ammortization(id: str):

    return 'Not implemented'


@router.get('/device/{id}/time_in_use')
async def calc_time_in_use(id: str):
    return 'Not implemented'


@router.get('/device/{id}/remaining_resource_until_check')
async def calc_remaining_time(id: str):
    return 'Not implemented'
