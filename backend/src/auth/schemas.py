from pydantic import BaseModel
from pydantic import EmailStr
from src.models import UserCredentialsPydantic


class UserCredentials(UserCredentialsPydantic):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserToken(BaseModel):
    access_token: str = "ACTUAL_TOKEN"
    token_type: str = "Bearer"
