from src.roles import schemas
from src.roles.schemas import PermissionsTypes

superuser_tables_premissions = schemas.PermissionsBase(
    table_name='*',
    permissions=[PermissionsTypes.ALL])

SUPERUSER = schemas.RoleCreate(
    role_name="SUPERUSER", access=[superuser_tables_premissions])
