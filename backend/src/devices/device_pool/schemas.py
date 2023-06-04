from .. import models
from tortoise.expressions import Q
from typing import List
from pydantic import BaseModel, validator
from typing import Optional


class DevicePoolBase(BaseModel):
    description: str
    specifications: List[dict]

    @validator('specifications')
    def check_specifications_is_not_empty(cls, v):
        for d in v:
            if d == {}:
                raise ValueError('pairs could not be empty')
        return v

    class Config():
        orm_mode = True


class DevicePoolPost(DevicePoolBase):
    pass


class DevicePoolGet(models.DevicePoolFullInfo, models.DeviceInfo):
    _id: str


class DevicePoolGetRequest(BaseModel):
    name: Optional[str]
    category: Optional[str]
    price: Optional[float]

    def generate_expression(cls):

        qs = []

        if cls.name is not None:
            qs.append(Q(name=cls.name))
        if cls.category is not None:
            qs.append(Q(category=cls.category))

        return qs
