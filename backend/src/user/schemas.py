from pydantic import BaseModel
from pydantic import EmailStr
from fastapi import status
from typing import List
import enum
from src.user.models import Genders
from datetime import date
from typing import Optional


class BaseUser(BaseModel):
    first_name: Optional[str]
    second_name: Optional[str]
    third_name: Optional[str]
    gender: Optional[Genders]
    datebirth: Optional[date]

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        use_enum_values = True
        arbitrary_types_allowed = True


class UserUpdate(BaseUser):
    pass


class UserSecuirityUpdate(BaseModel):
    password: Optional[str]
    email: Optional[EmailStr]
    phone_number: Optional[str]
    telegram_id: Optional[str]


class UserDeleteWithSecurity(BaseUser, UserSecuirityUpdate):

    class Config:
        orm_mode = True


class UserGet(BaseUser):
    username: str
    email: EmailStr
    telegram_id: Optional[str]
    phone_number: Optional[str]

    class Config:
        orm_mode = True


class TypesOfRestoreMethods(str, enum.Enum):
    TELEGRAM = "TELEGRAM"
    EMAIL = "EMAIL"
    PHONE_NUMBER = "PHONE_NUMBER"


class AvailableTypesOfRestoreMethods(BaseModel):
    methods: List[TypesOfRestoreMethods]


class UserNotFoundResponse(BaseModel):
    status_code: int = status.HTTP_404_NOT_FOUND
    message: str = "USER_NOT_FOUND"


class UserUpdatedResponse(BaseModel):
    status_code: int = status.HTTP_200_OK
    message: str = "USER_UPDATED"


class UserDeletedResposne(BaseModel):
    status_code: int = status.HTTP_200_OK
    message: str = "USER_DELETED"


class UserSecurityExceptionResponse(BaseModel):
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str = "AT_LEAST_ONE_CHANGE_PARAM_MUST_BE_NOT_NULL"


class UserAvailableResoreMethods(BaseModel):
    methods: List[TypesOfRestoreMethods]


class EmailAlreadyInUseResponse(BaseModel):
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str = "EMAIL_ALREADY_IN_USE"


class TelegramAlreadyInUseResponse(BaseModel):
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str = "EMAIL_ALREADY_IN_USE"


class PhoneNumberAlreadyInUseResponse(BaseModel):
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str = "EMAIL_ALREADY_IN_USE"


class DatebirthExceptionReponse(BaseModel):
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str
