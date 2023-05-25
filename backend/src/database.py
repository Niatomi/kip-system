from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.config import db_config

db_url = f'postgres://{db_config.db_user}:{db_config.db_pass}@{db_config.db_host}:{db_config.db_port}/{db_config.db_name}'
models = ["src.models", "aerich.models"]

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
