from pydantic import BaseModel


class ModufiedBaseModel(BaseModel):

    class Config:
        orm_mode = True


class GetParams(ModufiedBaseModel):
    category: str
    preson_id: str
    status: str
    place: str
