from tortoise import Tortoise
from typing import List
from pydantic import BaseModel, Field
from bson import ObjectId
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class DevicesPool(models.Model):
    """
    The Devices Pool model
    """

    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=50)
    check_intervals = fields.BigIntField()
    group = fields.CharField(max_length=30)
    price = fields.DecimalField(max_digits=20, decimal_places=2)
    resource = fields.IntField()

    active_devices = fields.ReverseRelation['ActiveDevices']


class ActiveDevices(models.Model):
    """
    The Active devices model
    """

    id = fields.UUIDField(pk=True)
    device_id: fields.ForeignKeyRelation[DevicesPool] = fields.ForeignKeyField(
        'models.DevicesPool', related_name='active_devices'
    )
    invent_number = fields.CharField(max_length=50)
    serial_number = fields.CharField(max_length=50)
    place = fields.CharField(max_length=60)


Tortoise.init_models([__name__], "models")
DevicePoolPydantic = pydantic_model_creator(DevicesPool,
                                            name='Device',
                                            exclude=['id', 'active_devices'])
ActiveDevicesPydantic = pydantic_model_creator(ActiveDevices)


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class DeviceInfo(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    description: str = Field(...)
    specifications: List[dict] = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
