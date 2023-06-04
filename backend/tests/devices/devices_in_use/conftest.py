import pytest
from httpx import AsyncClient


@pytest.fixture(scope="session")
async def device_1():
    return {
        "device_specs": {
            "description": "Description for device",
            "specifications": [
                {"spec1": "details"},
                {"spec2": "details"},
                {"spec3": "details"}
            ]
        },
        "device_info": {
            "name": "Device1",
            "check_intervals": 123123,
            "category": "category_1",
            "price": 1000.01,
            "resource": 123123,
            "resource_of_useful_usage": 5
        }
    }


@pytest.fixture(scope="session")
async def device_2():
    return {
        "device_specs": {
            "description": "Description for device",
            "specifications": [
                {"spec1": "details"},
                {"spec2": "details"},
                {"spec3": "details"}
            ]
        },
        "device_info": {
            "name": "Device2",
            "check_intervals": 123123,
            "category": "category_2",
            "price": 1000.01,
            "resource": 123123,
            "resource_of_useful_usage": 5
        }
    }


@pytest.fixture(scope="session")
async def device_id_1(admin_client_with_devices_in_pool: AsyncClient):
    r = await admin_client_with_devices_in_pool.get(
        '/device_pool/device',
        params={'name': 'Device1'}
    )
    return r.json()['id']


@pytest.fixture(scope='session')
async def responsible_person(admin_client_with_devices_in_pool: AsyncClient):
    person = {
        "username": "responsible",
        "first_name": "responsible",
        "second_name": "responsible",
        "third_name": "responsible",
        "full_name": "responsible",
        "email": "responsible@responsible.com",
        "password": "responsible"
    }
    await admin_client_with_devices_in_pool.post('/auth/sign_up',
                                                 json=person)


@pytest.fixture(scope="session")
async def device_id_2(admin_client_with_devices_in_pool: AsyncClient):
    r = await admin_client_with_devices_in_pool.get(
        '/device_pool/device',
        params={'name': 'Device2'}
    )
    return r.json()['id']


@pytest.fixture(scope="session")
async def admin_client_with_devices_in_pool(admin_client: AsyncClient,
                                            device_1: dict,
                                            device_2: dict):

    await admin_client.post('/device_pool/', json=device_1)
    await admin_client.post('/device_pool/', json=device_2)

    yield admin_client


@pytest.fixture(scope="session")
async def admin_client_with_active_devices(admin_client_with_devices_in_pool: AsyncClient,
                                           device_id_1: dict,
                                           device_id_2: dict):

    device_1 = {
        "invent_number": "123123",
        "serial_number": "123123",
        "place": "string1",
        "device_id": device_id_1
    }

    device_2 = {
        "invent_number": "string",
        "serial_number": "string",
        "place": "string2",
        "device_id": device_id_2
    }

    await admin_client_with_devices_in_pool.post('/devices_in_use/', json=device_1)
    await admin_client_with_devices_in_pool.post('/devices_in_use/', json=device_2)

    yield admin_client_with_devices_in_pool
