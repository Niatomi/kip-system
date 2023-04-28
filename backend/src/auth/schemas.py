from pydantic import BaseModel
from pydantic import EmailStr
from fastapi import status


class UserCredentials(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserToken(BaseModel):
    access_token: str = "ACTUAL_TOKEN"
    token_type: str = "Bearer"


class TokenData(BaseModel):
    id: str


class UserCreatedResponse(BaseModel):
    status_code: int = status.HTTP_201_CREATED
    message: str = "USER_CREATED"


class UserRestorePasswordsCreated(BaseModel):
    status_code: int = status.HTTP_201_CREATED
    message: str = "REQUEST_CREATED"


class InvalidCredentialsResponse(BaseModel):
    status_code: int = status.HTTP_403_FORBIDDEN
    message: str = "INVALID_CREDENTIALS"


class UserAlredyExistsResponse(BaseModel):
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str = "USER_ALREADY_EXISTS"


class UserNeedToReactivateAccountResponse(BaseModel):
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str = "USER_NEED_TO_REACTIVATE_ACCOUNT"
    

class MethodNotAllowedResponse(BaseModel):
    status_code: int = status.HTTP_405_METHOD_NOT_ALLOWED
    message: str = "METHOD_IS_NOT_ALLOWED_FOR_CURRENT_USER"
