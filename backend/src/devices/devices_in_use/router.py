from src.database import db
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi import APIRouter
from fastapi import Depends

from src.utils import check_user_is_not_worker
from . import schemas

router = APIRouter(prefix='/devices_in_use',
                   dependencies=[Depends(check_user_is_not_worker)],
                   tags=['Chief'])

# Many devices


@router.get('/')
async def get_devices_by_params_in_pages(
        params: schemas.GetParams = Depends(schemas.GetParams)):
    return 'Not implemented'


@router.get('/categories')
async def get_avaiable_categories():
    return 'Not implemented'


@router.get('/reposponsible_persons')
async def get_reponsible_presons():
    return 'Not implemented'


@router.get('/places')
async def get_places_of_installation():
    return 'Not implemented'


@router.get('/get_characteristics')
async def get_charachteristics():
    return 'Not implemented'


@router.get('/characteristics/{chrtcs}/')
async def get_devices_by_characteristsics(chrtcs: str):
    return 'Not implemented'

# One devices


@router.post('/')
async def add_device():
    return 'Not implemented'


@router.put('/device/{id}')
async def update_device(id: str):
    return 'Not implemented'


@router.get('/device/{id}')
async def get_device(id: str):
    return 'Not implemented'


@router.get('/device/{id}/ammortization')
async def calc_ammortization(id: str):
    return 'Not implemented'


@router.get('/device/{id}/time_in_use')
async def calc_time_in_use(id: str):
    return 'Not implemented'


@router.get('/device/{id}/remaining_resource_until_check')
async def calc_remaining_time(id: str):
    return 'Not implemented'
