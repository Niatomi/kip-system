from .models import DevicePoolPydantic
from typing import List


class DevicePoolPost(DevicePoolPydantic):
    description: str
    specifications: List[dict]

    class Config():
        orm_mode = True
