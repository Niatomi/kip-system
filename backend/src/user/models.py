from sqlalchemy import (
    Column,

    Date,
    TIMESTAMP,
    Integer,
    Boolean,
    String,
    JSON,
    CHAR,
    ForeignKey,
    func
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped


import enum
from uuid import uuid4 as uuid
from datetime import datetime
from datetime import date

from src.database import Base


class Genders(str, enum.Enum):
    MALE = "M"
    FEMALE = "F"


class User(Base):
    __tablename__ = 'users_table'
    id: Mapped[UUID] = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid,
        server_default=func.gen_random_uuid()
    )

    first_name: Mapped[str] = Column(String(32), nullable=True)
    second_name: Mapped[str] = Column(String(32), nullable=True)
    third_name: Mapped[str] = Column(String(32), nullable=True)

    gender: str = Column(
        'gender', CHAR, unique=False, nullable=True)
    datebirth: Mapped[date] = Column(Date, nullable=True, unique=False)

    username: Mapped[str] = Column(String, nullable=False, unique=True)
    password: Mapped[str] = Column(String, nullable=False)

    email: Mapped[str] = Column(String, nullable=True, unique=True)
    is_email_confirmed: Mapped[Boolean] = Column(
        Boolean, nullable=False, default=False)

    telegram_id: Mapped[str] = Column(String, nullable=True)
    is_telegram_id_confirmed: Mapped[Boolean] = Column(
        Boolean, nullable=False, default=False)

    phone_number: Mapped[str] = Column(String(25), unique=True)
    is_phone_number_confirmed: Mapped[Boolean] = Column(
        Boolean, nullable=False, default=False)

    role_id = Column(Integer, ForeignKey(
        'roles_table.id', ondelete='CASCADE'))

    created_at: Mapped[datetime] = Column(TIMESTAMP, default=datetime.utcnow)
    deleted_at: Mapped[datetime] = Column(TIMESTAMP, nullable=True)


class ProfilePhotos(Base):
    __tablename__ = 'profile_photos_table'
    user_id: Mapped[UUID] = Column(UUID(as_uuid=True), ForeignKey(
        "users_table.id", ondelete="CASCADE"), primary_key=True)


def get_empty_dict():
    return {}


class Questions(Base):
    __tablename__ = 'questions_table'
    user_id: Mapped[UUID] = Column(UUID(as_uuid=True), ForeignKey(
        "users_table.id", ondelete="CASCADE"), primary_key=True)
    questions_and_answers_file: Mapped[dict[str, any]] = Column(
        JSON, default=get_empty_dict)
