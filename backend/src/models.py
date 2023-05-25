from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


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


UserCredentialsPydantic = pydantic_model_creator(Users,
                                                 name="User",
                                                 exclude=['password_hash',
                                                          'email',
                                                          'id',
                                                          'created_at',
                                                          'modified_at'])
User_Pydantic = pydantic_model_creator(Users,
                                       name="User",
                                       exclude=['password_hash'])
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)
