from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Boolean, ForeignKey, Integer, String, Integer, TIMESTAMP
from config import DB_HOST, DB_PORT, DB_PASS, DB_USER, DB_NAME
from datetime import datetime

from sqlalchemy import JSON

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class Base(DeclarativeBase):
    pass


class Role(Base):
    __tablename__ = 'role_table'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    name: Mapped[str] = mapped_column(
        String, nullable=False
    )
    permissions: Mapped[dict] = mapped_column(
        JSON, nullable=True
    )


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user_table"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )

    username: Mapped[str] = mapped_column(
        "username", String, nullable=False
    )

    registration_date: Mapped[datetime] = mapped_column(
        "registration_date", TIMESTAMP, default=datetime.utcnow()
    )

    role_id: Mapped[int] = mapped_column(
        "role_id", Integer, ForeignKey(Role.id)
    )

    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )

    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )

    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
