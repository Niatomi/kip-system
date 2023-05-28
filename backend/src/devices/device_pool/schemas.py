from ..models import DevicePoolPydantic
from typing import List
from pydantic import BaseModel


class DevicePoolPost(BaseModel):
    description: str
    specifications: List[dict]

    class Config():
        orm_mode = True
