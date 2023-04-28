from sqlalchemy import MetaData

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.pool import NullPool

from sqlalchemy.orm import declarative_base

from typing import AsyncGenerator

from src.config import db_config

from sqlalchemy.ext.asyncio import AsyncSession

DATABASE_URL = f"postgresql+asyncpg://\
                {db_config.db_user}:\
                {db_config.db_pass}@\
                {db_config.db_host}:\
                {db_config.db_port}\
                /{db_config.db_name}"

engine = create_async_engine(
    DATABASE_URL, poolclass=NullPool, echo=db_config.ddl_show)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()
metadata = MetaData()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
