from bson.objectid import ObjectId
from src.database import mongo_db
from src.devices import models as device_models
import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_device_post_ok(admin_client: AsyncClient, device_1: dict):
    r = await admin_client.post('/device_pool/', json=device_1)

    assert r.status_code == 201

    device_from_db = await device_models.DevicesPool.filter(
        name=device_1["device_info"]['name']).first()

    assert device_from_db is not None
    device_from_db.name == device_1["device_info"]['name']

    mongo_device = await mongo_db.device_description.find_one(
        {"_id": ObjectId(oid=device_from_db.mongo_id)})
    assert mongo_device is not None
    assert mongo_device['specifications'] == device_1["device_specs"]['specifications']


@pytest.mark.anyio
async def test_device_duplicate_error(admin_client: AsyncClient, device_1: dict):
    r = await admin_client.post('/device_pool/', json=device_1)
    assert r.status_code == 422
    msg: str = r.json()['detail'][0]['msg']
    assert msg.startswith('duplicate key value violates unique constraint')
