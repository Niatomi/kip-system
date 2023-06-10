from typing import List
from fastapi import Query
from bson.objectid import ObjectId
from tortoise.expressions import Q
from src.database import mongo_db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi import APIRouter
from fastapi import Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.tortoise import paginate

from .. import models
from . import schemas
from src import utils
from tortoise.transactions import in_transaction

router = APIRouter(prefix='/device_pool',
                   dependencies=[Depends(utils.check_user_is_not_worker)],
                   tags=['Device Pool'])


@router.get('/', response_model=Page[models.DevicePoolFullInfoGet])
async def get_devices_in_pages():
    return await paginate(models.DevicesPool)


@router.post('/')
async def add_device_into_pool(device_specs: schemas.DevicePoolPost,
                               device_info: models.DevicePoolPydantic):

    async with in_transaction():
        device_info = device_info.dict()
        device_info['mongo_id'] = 'None'
        await models.DevicesPool.create(**device_info)

        new_device_info = await mongo_db.device_description.insert_one(
            jsonable_encoder(device_specs)
        )
        device_info['mongo_id'] = new_device_info.inserted_id
        await models.DevicesPool.filter(name=device_info.pop('name')).update(**device_info)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=None)


@router.get('/search',
            response_model=List[models.DevicePoolFullInfoGet])
async def find_by_name(name: str = Query()):
    return await models.DevicesPool.filter(name__contains=name).all()


@router.get('/device')
async def get_device_by_params(
        params: schemas.DevicePoolGetRequest = Depends(schemas.DevicePoolGetRequest)):
    if params.dict(exclude_none=True) == {}:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='At least one params required')
    return await models.DevicesPool.filter(Q(*params.generate_expression(),
                                             join_type='OR')).first()


@router.get('/device/{device_id}')
async def get_device_by_id(device_id: str):

    pg_device = await models.DevicesPool.filter(id=device_id).first()
    if pg_device is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Device not found')
    mongo_device = await mongo_db.device_description.find_one(
        {"_id": ObjectId(oid=pg_device.mongo_id)})
    if mongo_device is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Specs not found. Notify us please about this request')
    pg_dev = await models.DevicePoolFullInfo.from_tortoise_orm(pg_device)
    mongo_device.pop('_id')
    return schemas.DevicePoolGet(**pg_dev.dict(), **mongo_device)


@router.put('/{device_id}')
async def update_device_by_id(device_id,
                              device_info: models.DevicePoolPydantic,
                              device_specs: schemas.DevicePoolPost = None):
    pg_device = await models.DevicesPool.filter(id=device_id).first()
    if pg_device is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Device not found')

    async with in_transaction():
        device_info = device_info.dict()
        await models.DevicesPool.filter(id=device_id).update(**device_info)
        if device_specs is not None:
            mongo_info = device_specs.dict()
            await mongo_db.device_description.update_one(
                {"_id": ObjectId(pg_device.mongo_id)}, {"$set": mongo_info})
    return await get_device_by_id(device_id)
