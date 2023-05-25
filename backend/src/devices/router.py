from src.database import db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.exceptions import HTTPException
from .utils import get_user_role
from fastapi import APIRouter
from fastapi import Depends

from src.auth.oauth2 import get_current_user
from uuid import UUID
from src.models import Roles
from fastapi_pagination import (
    LimitOffsetPage,
    Page
)
from . import models
from . import schemas

router = APIRouter(prefix='/devices',
                   dependencies=[Depends(get_current_user)],
                   tags=['Devices'])


@router.post('/device_pool')
async def add_device_into_pool(device_info: schemas.DevicePoolPost,
                               role: Roles = Depends(get_user_role)):
    # if role != Roles.admin:
    #     raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
    #                         detail="User don't have permissions")
    device_info = device_info.dict()
    description = device_info.pop('description')
    specifications = device_info.pop('specifications')
    device_info = models.DeviceInfo(description=description, specifications=specifications)

    # await models.DevicesPool.create(device_info)

    device_info = jsonable_encoder(device_info)
    new_device_info = await db["device_description"].insert_one(device_info)
    created_device = await db["device_description"].find_one({"_id": new_device_info.inserted_id})
    print(created_device)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=None)


@router.get('/active_devices')
async def get_all_devices(role: Roles = Depends(get_user_role)):
    if role != Roles.chief:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                            detail="User don't have permissions")


@router.get('/active_pool/{device_id}')
async def get_active_device(device_id: UUID):
    return 'Not implemented'
