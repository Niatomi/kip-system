from src.database import db_url, models
import typer
from src import models as db_models
from src.auth.utils import hash

from tortoise import Tortoise, run_async

app = typer.Typer()


async def create_admin(username: str,
                       password: str,
                       email: str,
                       first_name: str = 'admin',
                       second_name: str = 'admin',
                       third_name: str = 'admin'):
    print(db_url)
    await Tortoise.init(db_url=db_url, modules={"models": models})
    await Tortoise.generate_schemas()
    await db_models.Users.create(
        username=username,
        password_hash=hash(password),
        email=email,
        first_name=first_name,
        second_name=second_name,
        third_name=third_name,
        role=db_models.Roles.admin
    )


@app.command()
def create(username: str,
           password: str,
           email: str,
           first_name: str = 'admin',
           second_name: str = 'admin',
           third_name: str = 'admin'):
    username = username
    password = password
    email = email
    first_name = first_name
    second_name = second_name
    third_name = third_name
    run_async(create_admin(username,
                           password,
                           email,
                           first_name,
                           second_name,
                           third_name))
    print('Admin created!')


if __name__ == "__main__":
    app()
