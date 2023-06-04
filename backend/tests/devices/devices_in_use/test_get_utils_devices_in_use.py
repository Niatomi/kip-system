# import pytest
# from httpx import AsyncClient


# @pytest.mark.anyio
# async def test_get_categories(admin_client_with_devices_in_pool: AsyncClient):
#     r = await admin_client_with_devices_in_pool.get('/devices_in_use/categories')
#     assert r.json() == ['spec1', 'spec2', 'spec3']


# @pytest.mark.anyio
# async def test_get_places(admin_client_with_active_devices: AsyncClient):
#     r = await admin_client_with_active_devices.get('/devices_in_use/places')
#     assert r.json() == ['string', 'string1', 'string2']
