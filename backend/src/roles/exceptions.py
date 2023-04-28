from fastapi import Request
from fastapi.responses import JSONResponse
from src.roles.schemas import (
    RoleAlreadyExistsResponse,
    RoleNotFoundReponse
)


class RoleAlreadyExistsException(Exception):
    pass


class RoleNotFoundException(Exception):
    pass


def role_already_exists_handler(request: Request, exc: RoleAlreadyExistsException):
    content = RoleAlreadyExistsResponse()
    return JSONResponse(status_code=content.status_code, content=content.dict())


def role_not_found_handler(request: Request, exc: RoleNotFoundException):
    content = RoleNotFoundReponse()
    return JSONResponse(status_code=content.status_code, content=content.dict())
