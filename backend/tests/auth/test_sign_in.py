from src.auth.schemas import UserToken
import pytest
from httpx import AsyncClient


user = {
    "username": "user_sign_in",
    "first_name": "string",
    "second_name": "string",
    "third_name": "string",
    "full_name": "string",
    "email": "user_sign_in@example.com",
    "password": "string"
}

user_credentials = {
    'username': user['username'],
    'password': user['password']
}


@pytest.mark.anyio
async def test_sign_in_ok(client: AsyncClient):
    r = await client.post("/auth/sign_up", json=user)
    r = await client.post("/auth/sign_in", data=user_credentials)
    token_scheme = UserToken(**r.json())
    assert token_scheme.token_type == 'Bearer'


@pytest.mark.anyio
async def test_sign_in_bad(client: AsyncClient):
    r = await client.post("/auth/sign_up", json=user)
    user_credentials = {
        'username': 'asfvasv',
        'password': 'asdvasdv'
    }
    r = await client.post("/auth/sign_in", data=user_credentials)
    assert r.status_code == 400
