from pydantic import BaseModel
from typing import List

from fastapi import status

from enum import Enum


class PermissionsTypes(str, Enum):
    ALL = "ALL",
    CREATE = "CREATE",
    READ = "READ",
    UPDATE = "UPDATE",
    DELETE = "DELETE"
    FAKE_DELETE = "FAKE_DELETE"


class PermissionsBase(BaseModel):
    table_name: str
    permissions: List[PermissionsTypes]


class RoleBase(BaseModel):
    role_name: str
    access: List[PermissionsBase]


class RoleCreate(RoleBase):
    pass


class RoleGet(RoleBase):
    pass


class RoleUpdate(RoleBase):
    pass


class RoleGetSu(RoleBase):
    id: int


class RoleGetUser(BaseModel):
    role_name: str


class RolesGet(BaseModel):
    roles: List[RoleGetSu]


class RoleAlreadyExistsResponse(BaseModel):
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str = "ROLE_ALREADY_EXISTS"


class RoleNotFoundReponse(BaseModel):
    status_code: int = status.HTTP_404_NOT_FOUND
    message: str = "ROLE_NOT_FOUND"
