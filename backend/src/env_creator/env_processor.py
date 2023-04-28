from src.config import env_config
from . import db_env


async def prepare_env():

    if env_config.env_name == 'test':
        await db_env.excecute_test_env()

    # Only creates roles
    # Table contains some data
    if env_config.env_name == 'dev':
        await db_env.excecute_dev_env()
        # await excecute()

    # Only creates roles
    elif env_config.env_name == 'pre-prod':
        pass

        # Only creates roles
        # Params checker actually
    elif env_config.env_name == 'prod':
        pass


async def init():
    await prepare_env()
