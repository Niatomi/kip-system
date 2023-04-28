from .schemas import (
    UserNotFoundResponse,
    UserSecurityExceptionResponse,

    EmailAlreadyInUseResponse,
    TelegramAlreadyInUseResponse,
    PhoneNumberAlreadyInUseResponse,

    DatebirthExceptionReponse
)
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import Request


class UserNotFoundException(Exception):
    pass


class SecuirityUpdateException(Exception):
    pass


class EmailAlreadyInUseException(Exception):
    pass


class TelegramAlreadyInUseException(Exception):
    pass


class PhoneNumberAlreadyInUseException(Exception):
    pass


class UserDateException(Exception):
    def __init__(self, message: str):
        self.message = message


def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    content = UserNotFoundResponse()
    return JSONResponse(status_code=content.status_code, content=content.dict())


def security_update_exception_handler(request: Request, exc: SecuirityUpdateException):
    content = UserSecurityExceptionResponse()
    return JSONResponse(status_code=content.status_code, content=content.dict())


def email_already_in_use_exception(request: Request, exc: EmailAlreadyInUseException):
    content = EmailAlreadyInUseResponse()
    return JSONResponse(status_code=content.status_code, content=content.dict())


def telegram_already_in_use_exception(request: Request, exc: TelegramAlreadyInUseException):
    content = TelegramAlreadyInUseResponse()
    return JSONResponse(status_code=content.status_code, content=content.dict())


def phone_already_in_use_exception(request: Request, exc: PhoneNumberAlreadyInUseException):
    content = PhoneNumberAlreadyInUseResponse()
    return JSONResponse(status_code=content.status_code, content=content.dict())


def user_datebirth_exception(request: Request, exc: UserDateException):
    content = DatebirthExceptionReponse(message=exc.message)
    return JSONResponse(status_code=content.status_code, content=content.dict())
