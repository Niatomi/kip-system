import pytest
from httpx import AsyncClient
from src.models import Users


user = {
    "username": "user_sign_up",
    "first_name": "string",
    "second_name": "string",
    "third_name": "string",
    "full_name": "string",
    "email": "user_sign_up@example.com",
    "password": "string"
}


@pytest.mark.anyio
async def test_sign_up_ok(client: AsyncClient):

    r = await client.post("/auth/sign_up", json=user)
    assert r.status_code == 201

    user_from_db = await Users.filter(username=user['username']).first()

    assert user_from_db.username == user['username']
    assert user_from_db.first_name == user['first_name']
    assert user_from_db.second_name == user['second_name']
    assert user_from_db.third_name == user['third_name']
    assert user_from_db.email == user['email']


@pytest.mark.anyio
async def test_sign_up_bad(client: AsyncClient):
    await client.post("/auth/sign_up", json=user)
    r = await client.post("/auth/sign_up", json=user)
    assert r.status_code == 400
    assert r.json()['detail'] == "User already exists"
