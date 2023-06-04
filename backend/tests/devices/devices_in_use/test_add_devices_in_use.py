# from uuid import uuid4
# import pytest
# from httpx import AsyncClient


# def device_in_use(device_id) -> dict:
#     return {
#         "invent_number": "string",
#         "serial_number": "string",
#         "place": "string",
#         "device_id": device_id
#     }


# @pytest.mark.anyio
# async def test_device_add_ok(admin_client_with_devices_in_pool: AsyncClient,
#                              device_id_1: str, device_1: dict):
#     device_1 = device_in_use(device_id_1)
#     r = await admin_client_with_devices_in_pool.post('/devices_in_use/',
#                                                      json=device_1)

#     assert r.json()['invent_number'] == device_1['invent_number']
#     assert r.json()['serial_number'] == device_1['serial_number']
#     assert r.json()['place'] == device_1['place']
#     assert r.json()['device_id'] == device_1['device_id']


# @pytest.mark.anyio
# async def test_device_add_no_device_in_pool(admin_client_with_devices_in_pool: AsyncClient,
#                                             device_id_1: str, device_1: dict):
#     device_id_1 = str(uuid4())
#     device_1 = device_in_use(device_id_1)

#     r = await admin_client_with_devices_in_pool.post('/devices_in_use/',
#                                                      json=device_1)
#     assert r.status_code == 422
#     assert r.json()['detail'][0]['msg'].startswith(
#         'insert or update on table "activedevices" violates foreign key')

# # Many devices
# # Get by category
# # Get by responsible users
# # Get responsible persons
# # Get devices that have on check status

# # Get by installed place
# # Get place in use

# # Get know characteristics
# # Get devices by charecteristic

# # One device
# # Get by time in use
# # Get remaining resorce
# # Count ammortization
