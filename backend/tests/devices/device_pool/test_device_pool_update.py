import pytest
from httpx import AsyncClient

update_schema = {
    "device_specs": {
        "description": "Description for device",
        "specifications": [
            {"spec1": "details"},
            {"spec2": "details"},
            {"spec3": "details"},
            {"spec4": "details"}
        ]
    },
    "device_info": {
        "name": "Device",
        "check_intervals": 10000,
        "group": "string",
        "price": 10000.01,
        "resource": 10000
    }
}


@pytest.mark.anyio
async def test_device_update_ok(admin_client: AsyncClient, device: dict):
    await admin_client.post('/device_pool/', json=device)
    r = await admin_client.get('/device_pool/device', params={'name': 'Device'})
    device_id = r.json()["id"]
    r = await admin_client.get(f'/device_pool/device/{device_id}')
    device_before = r.json()
    r = await admin_client.put(f'/device_pool/{device_id}', json=update_schema)
    r = await admin_client.get(f'/device_pool/device/{device_id}')
    device_after = r.json()

    assert device_before['resource'] != device_after['resource']
    assert device_after['resource'] == update_schema['device_info']['resource']

    assert device_before['specifications'] != device_after['specifications']
    assert update_schema["device_specs"]['specifications'] == device_after['specifications']


@pytest.mark.anyio
async def test_device_update_duplicate_bad(admin_client: AsyncClient, device: dict):
    await admin_client.post('/device_pool/', json=device)

    device = device.copy()
    device['device_info']['name'] = 'Device1'
    update_schema['device_info']['name'] = 'Device'
    await admin_client.post('/device_pool/', json=device)

    r = await admin_client.get('/device_pool/device', params={'name': 'Device1'})
    device_id = r.json()["id"]

    r = await admin_client.get(f'/device_pool/device/{device_id}')
    r = await admin_client.put(f'/device_pool/{device_id}', json=update_schema)
    assert r.json()['detail'][0]['msg'].startswith('duplicate key value violates unique constraint')
