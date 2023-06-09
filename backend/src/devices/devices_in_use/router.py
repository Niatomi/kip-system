from tortoise.expressions import Q
from ..utils import get_mongo_id_by_spec
from fastapi import Query
from datetime import timedelta
import datetime
from .utils import diff_month
from . import service
from uuid import UUID
from ..models import ActiveDevicesPydanticGet, DevicePoolFullInfo
from typing import List
from .utils import check_device_is_exists
from uuid import uuid4
from src.auth.oauth2 import get_current_user
from src.models import Users
from sqlalchemy.engine.result import ChunkedIteratorResult
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
from ..utils import get_mongo_object_by_id
from fastapi_pagination import Page
from fastapi_pagination.ext.tortoise import paginate


router = APIRouter(prefix='/devices_in_use',
                   dependencies=[Depends(check_user_is_not_worker)],
                   tags=['Devices In Use'])

# Many devices


@router.get('/pages',
            response_model=Page[models.ActiveDevicesPydanticGet])
async def get_device_in_pages():
    return await paginate(models.ActiveDevices)


@router.get('/search',
            response_model=List[models.ActiveDevicesPydanticGet])
async def find_by_name(name: str = Query()):
    return await models.ActiveDevices.filter(device__name__contains=name).all()


@router.get('/', response_model=List[schemas.DeviceInUseOut])
async def get_devices_by_params_in_pages(
        params: schemas.GetParams = Depends(schemas.GetParams),
        session: AsyncSession = Depends(get_session)):
    if (params.category is None and
        params.person_id is None and
        params.action is None and
            params.place is None):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='At least one argument must exists')
    result = []
    if params.category is not None:
        postgre_res = await models.ActiveDevices.filter(
            device__category=params.category).prefetch_related('device').all()
        for item in postgre_res:

            active_device_info = await ActiveDevicesPydanticGet.from_tortoise_orm(item)
            device_pool_info = await DevicePoolFullInfo.from_tortoise_orm(item.device)
            device_pool_info = device_pool_info.dict()
            device_pool_info.pop('id')
            device_pool_info.pop('active_devices')

            action = await session.execute(
                select(models.Events.action).order_by(
                    models.Events.created_at.desc()).filter(models.Events.device_id == item.id))
            action = {'current_action': action.scalar()}

            mongo_info = await get_mongo_object_by_id(device_pool_info['mongo_id'])
            mongo_info.pop('_id')
            device = {**active_device_info.dict(), **device_pool_info, **mongo_info, **action}

            result.append(device)
        return result

    if params.place is not None:
        postgre_res = await models.ActiveDevices.filter(
            place=params.place).prefetch_related('device').all()
        for item in postgre_res:

            active_device_info = await ActiveDevicesPydanticGet.from_tortoise_orm(item)
            device_pool_info = await DevicePoolFullInfo.from_tortoise_orm(item.device)
            device_pool_info = device_pool_info.dict()
            device_pool_info.pop('id')
            device_pool_info.pop('active_devices')

            action = await session.execute(
                select(models.Events.action).order_by(
                    models.Events.created_at.desc()).filter(models.Events.device_id == item.id))
            action = {'current_action': action.scalar()}

            mongo_info = await get_mongo_object_by_id(device_pool_info['mongo_id'])
            mongo_info.pop('_id')
            device = {**active_device_info.dict(), **device_pool_info, **mongo_info, **action}
            result.append(device)
        return result

    if params.person_id is not None:
        events = await session.execute(
            select(models.Events).order_by(models.Events.created_at.desc()).filter(
                models.Events.responsible_person == params.person_id)
        )
        current_devices = []
        for item in events.scalars():
            if not current_devices.count(item.device_id):
                current_devices.append(item.device_id)
        postgre_res = []

        for cd in current_devices:
            device = await models.ActiveDevices.filter(id=cd).prefetch_related('device').first()
            postgre_res.append(device)

        for item in postgre_res:

            active_device_info = await ActiveDevicesPydanticGet.from_tortoise_orm(item)
            device_pool_info = await DevicePoolFullInfo.from_tortoise_orm(item.device)
            device_pool_info = device_pool_info.dict()
            device_pool_info.pop('id')
            device_pool_info.pop('active_devices')

            action = await session.execute(
                select(models.Events.action).order_by(
                    models.Events.created_at.desc()).filter(models.Events.device_id == item.id))
            action = {'current_action': action.scalar()}

            mongo_info = await get_mongo_object_by_id(device_pool_info['mongo_id'])
            mongo_info.pop('_id')
            device = {**active_device_info.dict(), **device_pool_info, **mongo_info, **action}
            result.append(device)
        return result

    if params.action is not None:
        events = await session.execute(
            select(models.Events).order_by(models.Events.created_at.desc()).filter(
                models.Events.action == params.action)
        )
        current_devices = []
        for item in events.scalars():
            if not current_devices.count(item.device_id):
                current_devices.append(item.device_id)
        postgre_res = []

        for cd in current_devices:
            device = await models.ActiveDevices.filter(id=cd).prefetch_related('device').first()
            postgre_res.append(device)

        for item in postgre_res:

            active_device_info = await ActiveDevicesPydanticGet.from_tortoise_orm(item)
            device_pool_info = await DevicePoolFullInfo.from_tortoise_orm(item.device)
            device_pool_info = device_pool_info.dict()
            device_pool_info.pop('id')
            device_pool_info.pop('active_devices')

            action = await session.execute(
                select(models.Events.action).order_by(
                    models.Events.created_at.desc()).filter(models.Events.device_id == item.id))
            action = {'current_action': action.scalar()}

            mongo_info = await get_mongo_object_by_id(device_pool_info['mongo_id'])
            mongo_info.pop('_id')
            device = {**active_device_info.dict(), **device_pool_info, **mongo_info, **action}
            if action['current_action'] == params.action:
                result.append(device)
        return result

    return result


@router.get('/by_specification',
            response_model=List[schemas.DeviceInUseOut])
async def get_devices_by_specification(specifications: List[str] = Query(),
                                       session: AsyncSession = Depends(get_session)):
    mongo_ids = [await get_mongo_id_by_spec(spec) for spec in specifications]
    exp = [Q(device__mongo_id=id) for id in mongo_ids]
    postgre_res = await models.ActiveDevices.filter(Q(*exp, join_type='OR')).prefetch_related('device').all()
    result = []
    for item in postgre_res:

        active_device_info = await ActiveDevicesPydanticGet.from_tortoise_orm(item)
        device_pool_info = await DevicePoolFullInfo.from_tortoise_orm(item.device)
        device_pool_info = device_pool_info.dict()
        device_pool_info.pop('id')
        device_pool_info.pop('active_devices')

        action = await session.execute(
            select(models.Events.action).order_by(
                models.Events.created_at.desc()).filter(models.Events.device_id == item.id))
        action = {'current_action': action.scalar()}

        mongo_info = await get_mongo_object_by_id(device_pool_info['mongo_id'])
        mongo_info.pop('_id')
        device = {**active_device_info.dict(), **device_pool_info, **mongo_info, **action}

        result.append(device)
    return result


@router.get('/categories')
async def get_available_categories():

    all_categories = await models.DevicesPool.all().distinct().values('category')
    available_categories = []
    for category in all_categories:
        device = await models.ActiveDevices.filter(device__category=category['category']).first()
        if device is not None:
            available_categories.append(category['category'])

    return available_categories


@router.get('/specifications')
async def get_avaiable_specifications():
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
async def get_reponsible_presons(session: AsyncSession = Depends(get_session)):
    responsibles = await session.execute(
        select(models.Events.responsible_person).order_by(
            models.Events.created_at.desc()).distinct()
    )
    return [i for i in responsibles.scalars()]


@router.get('/actions')
async def get_status(session: AsyncSession = Depends(get_session)):
    query = select(models.Events.action).distinct('action')
    result: ChunkedIteratorResult = await session.execute(query)
    return [i for i in result.scalars()]


@router.get('/places')
async def get_places_of_installation():
    places = await models.ActiveDevices.all().distinct().values('place')
    return [p['place'] for p in places]

# One devices


@router.post('/')
async def add_device(device: models.ActiveDevicesPydanticPost,
                     responsible_person: str,
                     session: AsyncSession = Depends(get_session),
                     current_user: Users = Depends(get_current_user)):
    async with in_transaction():

        if await Users.filter(id=responsible_person).first() is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='Responsible not found')

        click_object = {
            'id': str(uuid4()),
            'device_id': str(uuid4()),
            'responsible_person': responsible_person,
            'action': 'REGISTRED',
            'created_by': str(current_user.id)
        }
        await session.execute(models.Events.__table__.insert(), click_object)
        device = device.dict()
        device['id'] = click_object['device_id']
        model = await models.ActiveDevices.create(**device)

    return model


@router.put('/device/{id}', dependencies=[Depends(check_device_is_exists)])
async def update_device(id: str, device: models.ActiveDevicesPydanticPost):
    async with in_transaction():
        await models.ActiveDevices.filter(id=id).update(**device.dict())
    return await models.ActiveDevices.filter(id=id).first()


@router.patch('/device/{id}', dependencies=[Depends(check_device_is_exists)])
async def apply_new_action(id: UUID,
                           action: str,
                           session: AsyncSession = Depends(get_session),
                           current_user: Users = Depends(get_current_user)):
    query = select(models.Events).order_by(
        models.Events.created_at.desc()
    ).filter(models.Events.device_id == id)

    events = await session.execute(query)
    event = events.scalar()

    click_object = {
        'id': str(uuid4()),
        'device_id': id,
        'responsible_person': event.responsible_person,
        'action': action.upper(),
        'created_by': str(current_user.id)
    }
    await session.execute(models.Events.__table__.insert(), click_object)


@router.get('/device/{id}',
            dependencies=[Depends(check_device_is_exists)],
            response_model=schemas.DeviceInUseOut)
async def get_device(id: str,
                     session: AsyncSession = Depends(get_session)):
    postgre_res = await models.ActiveDevices.filter(id=id).prefetch_related('device').first()
    active_device_info = await ActiveDevicesPydanticGet.from_tortoise_orm(postgre_res)
    device_pool_info = await DevicePoolFullInfo.from_tortoise_orm(postgre_res.device)
    device_pool_info = device_pool_info.dict()
    device_pool_info.pop('id')
    device_pool_info.pop('active_devices')

    action = await session.execute(
        select(models.Events.action).order_by(
            models.Events.created_at.desc()).filter(models.Events.device_id == postgre_res.id))
    action = {'current_action': action.scalar()}

    mongo_info = await get_mongo_object_by_id(device_pool_info['mongo_id'])
    mongo_info.pop('_id')
    device = {**active_device_info.dict(), **device_pool_info, **mongo_info, **action}
    return device


@router.get('/device/{id}/ammortization',
            dependencies=[Depends(check_device_is_exists)])
async def calc_ammortization(id: str,
                             session: AsyncSession = Depends(get_session)):

    query = select(models.Events).order_by(
        models.Events.created_at.asc()
    ).filter(models.Events.device_id == id)

    events = await session.execute(query)
    first_appear = events.scalar()

    query = select(models.Events).order_by(
        models.Events.created_at.desc()
    ).filter(models.Events.device_id == id)

    events = await session.execute(query)
    last_appear = events.scalar()
    months_in_use = diff_month(last_appear.created_at, first_appear.created_at)

    device = await models.ActiveDevices.filter(id=id).prefetch_related('device').first()
    device_pool: models.DevicesPool = device.device
    device_pool

    return service.calc_amortization(device_pool, months_in_use)


@router.get('/device/{id}/time_in_use',
            dependencies=[Depends(check_device_is_exists)])
async def calc_time_in_use(id: str,
                           session: AsyncSession = Depends(get_session)):
    query = select(models.Events).order_by(
        models.Events.created_at.asc()
    ).filter(models.Events.device_id == id)

    events = await session.execute(query)
    first_appear = events.scalar()

    query = select(models.Events).order_by(
        models.Events.created_at.desc()
    ).filter(models.Events.device_id == id)

    events = await session.execute(query)
    last_appear = events.scalar()
    return last_appear.created_at - first_appear.created_at


@router.get('/device/{id}/remaining_resource_until_check',
            dependencies=[Depends(check_device_is_exists)])
async def calc_remaining_time(id: str,
                              session: AsyncSession = Depends(get_session)):
    query = select(models.Events).order_by(
        models.Events.created_at.asc()
    ).filter(models.Events.device_id == id and
             (models.Events.action == 'REGISTRED'))
    first_appear = await session.execute(query)
    first_appear = first_appear.scalar()
    first_action = first_appear.created_at

    query = select(models.Events).order_by(
        models.Events.created_at.desc()
    ).filter(models.Events.device_id == id and
             (models.Events.action == 'CHECKED' or models.Events.action == 'REGISTRED'))
    last_action = await session.execute(query)
    last_action = last_action.scalar()
    last_check = last_action.created_at

    id = first_appear.device_id

    postgre_res = await models.ActiveDevices.filter(id=id).prefetch_related('device').first()
    active_device_info = await ActiveDevicesPydanticGet.from_tortoise_orm(postgre_res)
    device_pool_info = await DevicePoolFullInfo.from_tortoise_orm(postgre_res.device)
    device_pool_info = device_pool_info.dict()
    device_pool_info.pop('id')
    device_pool_info.pop('active_devices')

    action = await session.execute(
        select(models.Events.action).order_by(
            models.Events.created_at.desc()).filter(models.Events.device_id == postgre_res.id))
    action = {'current_action': action.scalar()}

    mongo_info = await get_mongo_object_by_id(device_pool_info['mongo_id'])
    mongo_info.pop('_id')
    device = {**active_device_info.dict(), **device_pool_info, **mongo_info, **action}

    delta = last_check - first_action
    remaing_time = (365 * device['resource']) - delta.days - device['check_intervals']
    return remaing_time // 365


@router.get('/next_check')
async def check_plan(session: AsyncSession = Depends(get_session)):
    query = select(models.Events).order_by(
        models.Events.created_at.desc()
    )
    objects = await session.execute(query)
    events = objects.scalars()
    last_events = []
    known_devices = []
    for event in events:
        if not known_devices.count(event.device_id):
            if event.action != 'ON_CHECK':
                continue
            known_devices.append(event.device_id)
            deviceInfo = await models.DevicesPool.filter(active_devices__id=event.device_id).first()

            probable_time = event.created_at + timedelta(days=deviceInfo.check_intervals)
            if probable_time < datetime.datetime.now():
                probable_time = 'NEEDS_CHECK'
            last_events.append({
                'device_id': event.device_id,
                'next_check_time': probable_time
            })
    return last_events


@router.get('/on_check')
async def on_check_status(session: AsyncSession = Depends(get_session)):
    query = select(models.Events).order_by(
        models.Events.created_at.desc()
    )
    objects = await session.execute(query)
    events = objects.scalars()
    last_events = []
    known_devices = []
    for event in events:

        if not known_devices.count(event.device_id):
            if event.action != 'ON_CHECK':
                known_devices.append(event.device_id)
                continue
            known_devices.append(event.device_id)
            last_events.append(event.device_id)
    return last_events


@router.get('/{id}/on_check',
            dependencies=[Depends(check_device_is_exists)])
async def get_next_check_on_device(id: str,
                                   session: AsyncSession = Depends(get_session)):
    query = select(models.Events).order_by(
        models.Events.created_at.desc()
    ).filter((models.Events.device_id == id))
    objects = await session.execute(query)
    event = objects.scalar()
    if event is None:
        return None
    if event.action == 'ON_CHECK':
        return None

    deviceInfo = await models.DevicesPool.filter(active_devices__id=event.device_id).first()
    probable_time = event.created_at + timedelta(days=deviceInfo.check_intervals)
    if probable_time < datetime.datetime.now():
        probable_time = 'NEEDS_CHECK'
    return probable_time
