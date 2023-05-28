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

router = APIRouter(prefix='/active_devices',
                   dependencies=[Depends(get_current_user)],
                   tags=['Active Devices'])


@router.get('/')
async def get_all_devices(role: Roles = Depends(get_user_role)):
    if role != Roles.chief:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                            detail="User don't have permissions")


@router.get('/active_pool/{device_id}')
async def get_active_device(device_id: UUID):
    return 'Not implemented'
