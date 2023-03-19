from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from datetime import datetime

class Base(DeclarativeBase):
    pass

class Operation(Base):
    __tablename__ = "operation_table"
    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True,
        autoincrement=True
    )
    
    quantity: Mapped[int] = mapped_column(
        Integer, 
        nullable=False
    )
    
    figi: Mapped[str] = mapped_column(
        String, 
        nullable=False
    )
    
    date: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), 
        default=datetime.utcnow()
    )
    
    type: Mapped[str] = mapped_column(
        String,
    )
    
