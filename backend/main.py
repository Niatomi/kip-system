from src.app.auth.database import User
from src.app.auth.auth import auth_backend

from src.app.auth.manager import get_user_manager

from src.app.auth.schemas import UserCreate
from src.app.auth.schemas import UserRead

from fastapi import FastAPI
from fastapi import Depends
import uvicorn
import configparser
from fastapi_users import FastAPIUsers

app = FastAPI(
    title="КИП",
    description="Приложение для учёта КИП процессов",
    version="0.0.1"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],

)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


@app.get('/protected-request')
def protected_request(user: User = Depends(current_user)):
    return f"Hello, dear {user.username}"


@app.get('/unprotected-request')
def unprotected_request():
    return "Hello, random fella"


def main():
    config = configparser.ConfigParser()
    config.read('./src/config/config.ini')

    is_dev = config.getboolean('dev', 'is_dev')
    port = config.getint('app', 'port')
    host = config.get('app', 'host')

    uvicorn.run("main:app", reload=is_dev, port=port, host=host)


if __name__ == "__main__":
    main()
