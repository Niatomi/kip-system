from tortoise import Tortoise
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from enum import Enum


class Roles(str, Enum):
    admin = 'ADMIN'
    chief = 'CHIEF'
    worker = 'WORKER'


class Users(models.Model):
    """
    The User model
    """

    id = fields.UUIDField(pk=True)

    username = fields.CharField(max_length=20, unique=True)
    password_hash = fields.CharField(max_length=128, null=True)
    email = fields.CharField(max_length=50, null=False)

    first_name = fields.CharField(max_length=50, null=True)
    second_name = fields.CharField(max_length=50, null=True)
    third_name = fields.CharField(max_length=50, null=True)

    chief_id = fields.UUIDField(null=True)

    role = fields.CharEnumField(Roles, null=True, default=Roles.worker)

    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def full_name(self) -> str:
        name = f'{self.first_name} {self.second_name} '
        if self.third_name:
            name += self.third_name
        return name.strip()

    class PydanticMeta:
        computed = ["full_name"]
        exclude = ["password_hash"]


Tortoise.init_models([__name__], "models")
UserCredentialsPydantic = pydantic_model_creator(Users,
                                                 name="UserCredentials",
                                                 include=[
                                                     'username',
                                                     'first_name',
                                                     'second_name',
                                                     'third_name',
                                                     'role'
                                                 ])
UserTyperPydantic = pydantic_model_creator(Users,
                                           name='UserTyper',
                                           include=['password_hash'])
UserOutPydantic = pydantic_model_creator(Users,
                                         name='UserOut',
                                         exclude=['password_hash'],
                                         )

UserInPydantic = pydantic_model_creator(Users,
                                        name="UserIn",
                                        exclude_readonly=True)
