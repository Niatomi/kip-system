from sqlalchemy import (
    Column,
    JSON,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import Mapped

from src.database import Base

from src.settings.utils import get_base_settings
import enum


class Themes(str, enum.Enum):
    DARK = "DARK"
    WHITE = "WHITE"


class Settings(Base):
    __tablename__ = 'settings_table'
    user_id: Mapped[UUID] = Column(UUID(as_uuid=True), ForeignKey(
        "users_table.id", ondelete="CASCADE"), primary_key=True)

    # TODO: ADD THEME ENUM

    front_file: Mapped[dict[str, any]] = Column(
        JSON, default=get_base_settings)
