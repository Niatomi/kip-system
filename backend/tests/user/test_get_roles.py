import pytest
from httpx import AsyncClient
from src.users.router import roles


@pytest.mark.anyio
async def get_roles(admin_client: AsyncClient):
    r = await admin_client.get('/users/')
    assert r.json() == roles
