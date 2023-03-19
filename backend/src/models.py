from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy import JSON
from sqlalchemy import ForeignKey
from sqlalchemy import Boolean

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from datetime import datetime

Base = declarative_base()


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


class User(Base):
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
