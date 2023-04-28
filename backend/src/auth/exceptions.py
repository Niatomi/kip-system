from .schemas import (
    InvalidCredentialsResponse,
    UserAlredyExistsResponse,
    UserNeedToReactivateAccountResponse,
    MethodNotAllowedResponse
)
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import Request


class InvalidCredentialsException(Exception):
    pass


class UserAlreadyExistsException(Exception):
    pass


class UserNeedToReactivateAccountException(Exception):
    pass


class MethodNotAllowedException(Exception):
    pass


def invalid_credentials_exception_handler(request: Request, exc: InvalidCredentialsException):
    content = InvalidCredentialsResponse()
    return JSONResponse(status_code=content.status_code, content=content.dict())


def user_already_exists_exception_handler(request: Request, exc: UserAlreadyExistsException):
    content = UserAlredyExistsResponse()
    return JSONResponse(status_code=content.status_code, content=content.dict())


def user_need_to_reactivate_account_exception_handler(request: Request, exc: UserNeedToReactivateAccountException):
    content = UserNeedToReactivateAccountResponse()
    return JSONResponse(status_code=content.status_code, content=content.dict())


def method_not_allowed_method_handler(request: Request, exc: MethodNotAllowedException):
    content = MethodNotAllowedResponse()
    return JSONResponse(status_code=content.status_code, content=content.dict())
