from pydantic import BaseModel, validator
from typing import Optional


class ModufiedBaseModel(BaseModel):

    class Config:
        orm_mode = True


class GetParams(ModufiedBaseModel):
    category: Optional[str]
    preson_id: Optional[str]
    action: Optional[str]
    place: Optional[str]

    @validator("category")  # validates all fields
    def validate_if_float(cls, value):

        if (cls.category is None and
            cls.preson_id is None and
            cls.status is None and
                cls.place is None):
            raise ValueError('At least one param required')

        return value
