from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import AuthenticationBackend, JWTStrategy
from config import SECRET

from fastapi_users import FastAPIUsers
from auth.manager import get_user_manager
from auth.models import User

cookie_transport = CookieTransport(
    cookie_max_age=3600, cookie_name="user_cookie")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],

)
