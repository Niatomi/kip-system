import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_get_users_in_pages(admin_with_users: AsyncClient):
    r = await admin_with_users.get('/users/')
    assert r.json()['items'] != []


@pytest.mark.anyio
async def test_get_users_in_pages_only_workers(admin_with_users: AsyncClient):
    r = await admin_with_users.get('/users/', params={'role': 'WORKER'})
    for item in r.json()['items']:
        assert item['role'] == 'WORKER'


@pytest.mark.anyio
async def test_get_users_in_pages_with_unknown_role(admin_with_users: AsyncClient):
    r = await admin_with_users.get('/users/', params={'role': '12334'})
    assert r.status_code == 400
    assert r.json()['detail'] == "Role doesn't exist"
