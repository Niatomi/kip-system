from uuid import uuid4
import pytest
from httpx import AsyncClient


@pytest.mark.anyio
@pytest.mark.parametrize("params",
                         [
                             {'name': 'Device'},
                             {'category': 'string'},
                             {
                                 'name': 'Device',
                                 'category': 'string'
                             },
                         ])
async def test_device_get_ok(admin_client: AsyncClient, device_1: dict, params):
    await admin_client.post('/device_pool/', json=device_1)
    r = await admin_client.get('/device_pool/device', params=params)
    assert r.status_code == 200
    assert r.json()['name'] == device_1['device_info']['name']


@pytest.mark.anyio
async def test_device_post_get_no_params(admin_client: AsyncClient, device_1: dict):
    await admin_client.post('/device_pool/', json=device_1)
    r = await admin_client.get('/device_pool/device')
    assert r.status_code == 400
    assert r.json()['detail'] == 'At least one params required'


@pytest.mark.anyio
async def test_device_get_by_id_ok(admin_client: AsyncClient, device_1: dict):
    await admin_client.post('/device_pool/', json=device_1)
    r = await admin_client.get('/device_pool/device', params={'name': 'Device'})
    assert r.status_code == 200
    r = await admin_client.get(f'/device_pool/device/{r.json()["id"]}', params={'name': 'Device'})
    assert r.status_code == 200
    assert r.json() is not None
    assert r.json()['description'] == 'Description for device'


@pytest.mark.anyio
async def test_device_get_bad(admin_client: AsyncClient, device_1: dict):
    r = await admin_client.get(f'/device_pool/device/{uuid4()}', params={'name': 'Device'})
    assert r.status_code == 400
    assert r.json()['detail'] == 'Device not found'
