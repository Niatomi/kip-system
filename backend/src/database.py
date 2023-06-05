from .config import clickhouse_db_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from .config import api_config
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.config import (
    postgres_db_config,
    mongo_db_config
)
from motor.motor_asyncio import AsyncIOMotorClient

mongo_url = 'mongodb://' + \
    f'{mongo_db_config.mongo_username}:{mongo_db_config.mongo_password}@' + \
    f'{mongo_db_config.mongo_db_host}:27017/{mongo_db_config.database_name}?retryWrites=true&w=majority'

client = AsyncIOMotorClient(mongo_url)
mongo_db = client[f'{mongo_db_config.database_name}']

db_url = 'postgres://' + \
    f'{postgres_db_config.postgres_user}:{postgres_db_config.postgres_password}@' + \
    f'{postgres_db_config.postgres_host}:{postgres_db_config.postgres_port}/' + \
    f'{postgres_db_config.postgres_db_name}'
models = ["src.models", "src.devices.models", "aerich.models"]
TORTOISE_ORM = {
    "connections": {"default": db_url},
    "apps": {
        "models": {
            "models": models,
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=db_url,
        modules={"models": models},
        generate_schemas=False,
        add_exception_handlers=True,
    )


clickhouse_url = 'clickhouse+asynch://' + \
    f'{clickhouse_db_config.clickhouse_user}:{clickhouse_db_config.clickhouse_password}@' + \
    f'{clickhouse_db_config.clickhouse_host}:9000/' + \
    f'{clickhouse_db_config.clickhouse_db_name}'
engine = create_async_engine(clickhouse_url)
Base = declarative_base()
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

if api_config.is_dev:
    print(mongo_url)
    print(db_url)
    print(clickhouse_url)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
