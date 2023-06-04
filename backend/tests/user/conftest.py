import pytest
from httpx import AsyncClient


@pytest.fixture(scope="session")
async def worker_1():
    return {
        "username": "worker_1",
        "password": "worker_1",
        "email": "worker_1@example.com",
        "first_name": "worker_1",
        "second_name": "worker_1",
        "third_name": "worker_1",
        "role": "WORKER"
    }


@pytest.fixture(scope="session")
async def worker_2():
    return {
        "username": "worker_2",
        "password": "worker_2",
        "email": "worker_2@example.com",
        "first_name": "worker_2",
        "second_name": "worker_2",
        "third_name": "worker_2",
        "role": "WORKER"
    }


@pytest.fixture(scope="session")
async def worker_3():
    return {
        "username": "worker_3",
        "password": "worker_3",
        "email": "worker_3@example.com",
        "first_name": "worker_3",
        "second_name": "worker_3",
        "third_name": "worker_3",
        "role": "WORKER"
    }


@pytest.fixture(scope="session")
async def admin_1():
    return {
        "username": "admin_1",
        "password": "admin_1",
        "email": "admin_1@example.com",
        "first_name": "admin_1",
        "second_name": "admin_1",
        "third_name": "admin_1",
        "role": "ADMIN"
    }


@pytest.fixture(scope="session")
async def chief_1():
    return {
        "username": "chief_1",
        "password": "chief_1",
        "email": "chief_1@example.com",
        "first_name": "chief_1",
        "second_name": "chief_1",
        "third_name": "chief_1",
        "role": "CHIEF"
    }


@pytest.fixture(scope="session")
async def admin_with_users(admin_client: AsyncClient,
                           worker_1: dict,
                           worker_2: dict,
                           worker_3: dict,
                           admin_1: dict,
                           chief_1: dict):

    await admin_client.post('/users/user', json=worker_1)
    await admin_client.post('/users/user', json=worker_2)
    await admin_client.post('/users/user', json=worker_3)
    await admin_client.post('/users/user', json=admin_1)
    await admin_client.post('/users/user', json=chief_1)

    yield admin_client
