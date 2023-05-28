from src.database import db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.exceptions import HTTPException
from src.utils import get_user_role
from fastapi import APIRouter
from fastapi import Depends

from src.auth.oauth2 import get_current_user
from uuid import UUID
from src.models import Roles
from .. import models
from . import schemas

router = APIRouter(prefix='/device_pool',
                   dependencies=[Depends(get_current_user)],
                   tags=['Device Pool'])


@router.post('/')
async def add_device_into_pool(device_specs: schemas.DevicePoolPost,
                               device_info: models.DevicePoolPydantic,
                               role: Roles = Depends(get_user_role)):
    # if role != Roles.admin:
    #     raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
    #                         detail="User don't have permissions")

    await models.DevicesPool.create(**device_info.dict())

    device_info = jsonable_encoder(device_specs)
    new_device_info = await db["device_description"].insert_one(
        device_info
    )
    created_device = await db["device_description"].find_one({"_id": device_info.inserted_id})
    print(created_device)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=None)
