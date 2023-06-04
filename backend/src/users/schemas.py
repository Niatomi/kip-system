from tortoise.expressions import Q
from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional


class UserCredentials(BaseModel):
    username: str
    password: str
    email: EmailStr
    first_name: str
    second_name: str
    third_name: str
    role: str


class UsersGetParams(BaseModel):

    user_id: Optional[UUID]
    username: Optional[str]
    email: Optional[EmailStr]

    @property
    def expression(self):
        qs = []
        if self.user_id is not None:
            qs.append(Q(id=self.user_id))
        if self.role is not None:
            qs.append(Q(id=self.role))
        if self.username is not None:
            qs.append(Q(username=self.username))
        if self.email is not None:
            qs.append(Q(email=self.email))

        if qs == []:
            raise ValueError('At least one argument must exists')

        return Q(*qs, join_type='AND')

    class Config():
        orm_mode = True
