from pydantic import BaseModel
from datetime import datetime
from datetime import timezone


class OperationCreate(BaseModel):
    quantity: int
    figi: str
    date: datetime
    type: str