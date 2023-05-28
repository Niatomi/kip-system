from src.database import client as mongo_client
from src.database import db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.exceptions import HTTPException
from src.utils import get_user_role
from fastapi import APIRouter
from fastapi import Depends

from src.auth.oauth2 import get_current_user
from src.models import Roles
from .. import models
from . import schemas
from tortoise.transactions import in_transaction

router = APIRouter(prefix='/device_pool',
                   dependencies=[Depends(get_current_user)],
                   tags=['Device Pool'])


@router.post('/')
async def add_device_into_pool(device_specs: schemas.DevicePoolPost,
                               device_info: models.DevicePoolPydantic,
                               role: Roles = Depends(get_user_role)):
    if role != Roles.admin:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                            detail="User don't have permissions")

    async with in_transaction():
        async with mongo_client.start_session as s:
            async with s.start_transaction():
                new_device_info = await db.device_description.insert_one(
                    jsonable_encoder(device_specs)
                )
        device_info = device_info.dict()
        device_info['mongo_id'] = new_device_info.inserted_id

        await models.DevicesPool.create(**device_info.dict())

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=None)


@router.get('/')
async def get_device_by_name(device_specs: schemas.DevicePoolPost,
                             device_info: models.DevicePoolPydantic,
                             role: Roles = Depends(get_user_role)):
    # if role != Roles.admin:
    #     raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
    #                         detail="User don't have permissions")

    async with in_transaction():
        async with mongo_client.start_session as s:
            async with s.start_transaction():
                new_device_info = await db.device_description.insert_one(
                    jsonable_encoder(device_specs)
                )
        device_info = device_info.dict()
        device_info['mongo_id'] = new_device_info.inserted_id

        await models.DevicesPool.create(**device_info.dict())

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=None)
