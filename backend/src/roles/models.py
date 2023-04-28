from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
)

from typing import List

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from src.database import Base

from src.user.models import (
    User,
    Genders,
    ProfilePhotos,
    Questions,
)


class Role(Base):
    __tablename__ = 'roles_table'
    id: Mapped[int] = Column(Integer, autoincrement=True, primary_key=True)
    role_name: Mapped[str] = Column(String(10), nullable=False, unique=True)
    permissions: Mapped[dict] = Column(JSON, nullable=False)
    users = relationship('User')
