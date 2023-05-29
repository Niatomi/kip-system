from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.config import (
    db_config,
    mongo_db_config
)
from motor.motor_asyncio import AsyncIOMotorClient

mongo_url = 'mongodb://' + \
    f'{mongo_db_config.mongo_username}:{mongo_db_config.mongo_password}@' + \
    f'localhost:27017/{mongo_db_config.database_name}?retryWrites=true&w=majority'
print(mongo_url)

client = AsyncIOMotorClient(mongo_url)
db = client[f'{mongo_db_config.database_name}']

db_url = 'postgres://' + \
    f'{db_config.db_user}:{db_config.db_pass}@' + \
    f'{db_config.db_host}:{db_config.db_port}/{db_config.db_name}'
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
