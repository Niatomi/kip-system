from src.auth.schemas import UserToken
import pytest
from httpx import AsyncClient


user = {
    "username": "user_refresh_token",
    "first_name": "string",
    "second_name": "string",
    "third_name": "string",
    "full_name": "string",
    "email": "user_refresh_token@example.com",
    "password": "string"
}

user_credentials = {
    'username': user['username'],
    'password': user['password']
}


@pytest.mark.anyio
async def test_refresh_token_ok(client: AsyncClient):
    r = await client.post("/auth/sign_up", json=user)
    r = await client.post("/auth/sign_in", data=user_credentials)
    token_scheme = UserToken(**r.json())
    r = await client.put("/auth/refresh_token", json=token_scheme.dict())
    assert r.status_code == 200


@pytest.mark.anyio
async def test_refresh_token_bad(client: AsyncClient):
    r = await client.post("/auth/sign_up", json=user)
    r = await client.post("/auth/sign_in", data=user_credentials)
    token_scheme = UserToken(**r.json())
    token_scheme.access_token = 'asldknfalsjkrnvlrjknv'
    r = await client.put("/auth/refresh_token", json=token_scheme.dict())
    assert r.status_code == 401
