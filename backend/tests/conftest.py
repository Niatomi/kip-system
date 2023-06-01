from src.auth.schemas import UserToken
from src.models import Roles
from src.models import Users
from src.database import db
import asyncio
import pytest
from httpx import AsyncClient
from tortoise import Tortoise

from src.__main__ import app
from src.database import db_url, models

DB_URL = db_url


async def init_db(db_url, create_db: bool = False, schemas: bool = False) -> None:
    """Initial database connection"""
    await Tortoise.init(
        db_url=db_url, modules={"models": models}, _create_db=create_db
    )
    if create_db:
        print(f"Database created! {db_url = }")
    if schemas:
        await Tortoise.generate_schemas()
        print("Success to generate schemas")


async def init(db_url: str = DB_URL):
    await init_db(db_url, True, True)


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(app=app, base_url="http://test/v1") as client:
        yield client


@pytest.fixture(scope="session")
async def admin_client():
    async with AsyncClient(app=app, base_url="http://test/v1") as client:

        admin = {
            "username": "admin",
            "first_name": "admin",
            "second_name": "admin",
            "third_name": "admin",
            "full_name": "admin",
            "email": "admin@example.com",
            "password": "admin",
        }
        admin_credentials = {
            'username': 'admin',
            'password': 'admin'
        }
        r = await client.post("/auth/sign_up", json=admin)
        await Users.filter(username='admin').update(role=Roles.admin)
        r = await client.post("/auth/sign_in", data=admin_credentials)
        token_scheme = UserToken(**r.json())
        client.headers = {"Authorization": f"Bearer {token_scheme.access_token}"}
        yield client


@pytest.fixture(scope="session", autouse=True)
async def initialize_tests():
    await init()
    yield
    await db.device_description.drop()
    await Tortoise._drop_databases()


@pytest.fixture(scope="session")
def event_loop():
    """Overrides pytest default function scoped event loop"""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()
