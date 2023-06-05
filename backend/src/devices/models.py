from datetime import datetime
from src.database import Base
from uuid import uuid4
from sqlalchemy import Column
from clickhouse_sqlalchemy import (
    types, engines
)
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
    mongo_id = fields.CharField(max_length=25)
    name = fields.CharField(max_length=150, unique=True)
    check_intervals = fields.IntField()
    category = fields.CharField(max_length=30)
    price = fields.DecimalField(max_digits=20, decimal_places=2)

    resource = fields.IntField()
    resource_of_useful_usage = fields.IntField(default=5)

    active_devices = fields.ReverseRelation['ActiveDevices']


class ActiveDevices(models.Model):
    """
    The Active devices model
    """

    id = fields.UUIDField(pk=True)
    device: fields.ForeignKeyRelation[DevicesPool] = fields.ForeignKeyField(
        'models.DevicesPool', related_name='active_devices', to_field='id', unique=False
    )
    invent_number = fields.CharField(max_length=50)
    serial_number = fields.CharField(max_length=50)
    place = fields.CharField(max_length=60, unique=False)


Tortoise.init_models([__name__], "models")
DevicePoolPydantic = pydantic_model_creator(DevicesPool,
                                            name='Device',
                                            exclude=['id',
                                                     'active_devices',
                                                     'mongo_id'])
DevicePoolFullInfo = pydantic_model_creator(DevicesPool,
                                            name="DeviceFullInfo")
DevicePoolFullInfoGet = pydantic_model_creator(DevicesPool,
                                               name="DeviceFullInfoGet",
                                               exclude=['active_devices'])

ActiveDevicesPydantic = pydantic_model_creator(ActiveDevices,
                                               name='ActiveDevice',
                                               exclude=('id', 'device',)
                                               )
ActiveDevicesPydanticPost = pydantic_model_creator(ActiveDevices,
                                                   name='ActiveDevicePost',
                                                   exclude=('id', 'device',))
ActiveDevicesPydanticGet = pydantic_model_creator(ActiveDevices,
                                                  name='ActiveDeviceGet',
                                                  exclude=['device'])


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


class UpdateDeviceInfo(BaseModel):
    description: str = Field(...)
    specifications: List[dict] = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class Events(Base):
    __tablename__ = 'events'
    id = Column(types.UUID, primary_key=True, default=uuid4)
    device_id = Column(types.UUID, nullable=False)
    responsible_person = Column(types.UUID, nullable=False)
    action = Column(types.String, nullable=False)
    created_by = Column(types.UUID, nullable=False)
    created_at = Column(types.DateTime, nullable=False, default=datetime.utcnow)

    __table_args__ = (
        engines.MergeTree(),
    )
