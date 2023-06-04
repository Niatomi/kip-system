import pytest
from httpx import AsyncClient
from src.models import Users


@pytest.mark.anyio
async def test_add_user_ok(admin_client: AsyncClient,
                           worker_1: dict,
                           admin_1: dict,
                           chief_1: dict
                           ):
    r = await admin_client.post('/users/user', json=worker_1)
    assert r.status_code == 201

    us = await Users.get(username=worker_1['username'])
    assert us is not None


@pytest.mark.anyio
async def test_add_user_chief_add_admin_bad(chief_client: AsyncClient,
                                            admin_1: dict):
    r = await chief_client.post('/users/user', json=admin_1)
    assert r.status_code == 405


@pytest.mark.anyio
async def test_add_user_worker_add_admin_bad(worker_client: AsyncClient,
                                             admin_1: dict):
    r = await worker_client.post('/users/user', json=admin_1)
    assert r.status_code == 405


@pytest.mark.anyio
async def test_add_user_worker_add_chief_bad(worker_client: AsyncClient,
                                             chief_1: dict):
    r = await worker_client.post('/users/user', json=chief_1)
    assert r.status_code == 405


@pytest.mark.anyio
async def test_add_user_not_know_role_bad(admin_client: AsyncClient,
                                          admin_1: dict):
    admin_1['role'] = 'awoirhngeurg'
    r = await admin_client.post('/users/user', json=admin_1)
    assert r.status_code == 400
