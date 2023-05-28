import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_testpost(client: AsyncClient):
    r = await client.get("/ping")
    assert r.status_code == 200
