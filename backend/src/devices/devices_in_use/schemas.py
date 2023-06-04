from uuid import UUID
from pydantic import BaseModel
from typing import Optional
from ..models import ActiveDevicesPydanticGet, DevicePoolFullInfoGet
from typing import List


class ModifiedBaseModel(BaseModel):

    class Config:
        orm_mode = True


class DeviceInUseOut(ModifiedBaseModel,
                     ActiveDevicesPydanticGet,
                     DevicePoolFullInfoGet):
    description: str
    specifications: List[dict]
    current_action: str


class GetParams(ModifiedBaseModel):
    category: Optional[str]
    person_id: Optional[UUID]
    action: Optional[str]
    place: Optional[str]
