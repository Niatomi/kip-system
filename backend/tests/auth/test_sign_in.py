import pytest
from httpx import AsyncClient
from tortoise.backends.base.client import BaseDBAsyncClient


@pytest.mark.asyncio
async def test_get_something(async_client: AsyncClient, conn: BaseDBAsyncClient) -> None:
    # await conn.execute_query
    # response = await async_client.get("/something?skip=0&limit=5")

    # assert response.status_code == status.HTTP_200_OK
    # assert 0 < len(response.json()) <= 5
    pass
