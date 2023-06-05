from uuid import uuid4
from src.models import Users
from src.auth.utils import hash

_admin = {
    'username': 'admin',
    'password_hash': hash('admin'),
    'email': 'admin@example.com',
    'first_name': 'Виктор',
    'second_name': 'Викторов',
    'third_name': 'Викторович',
    'role': 'ADMIN'
}

chief_id = uuid4()
_chief = {
    'id': chief_id,
    'username': 'chief',
    'password_hash': hash('chief'),
    'email': 'chief@example.com',
    'first_name': 'Максим',
    'second_name': 'Максимов',
    'third_name': 'Максимович',
    'role': 'CHIEF'
}

_worker = {
    'username': 'worker',
    'password_hash': hash('worker'),
    'email': 'worker@example.com',
    'first_name': 'Иван',
    'second_name': 'Иванов',
    'third_name': 'Иванович',
    'chief_id': chief_id,
    'role': 'WORKER'
}


async def init_users():
    await Users.create(**_admin)
    await Users.create(**_chief)
    await Users.create(**_worker)

    admin = await Users.filter(username='admin').first()
    chief = await Users.filter(username='chief').first()
    worker = await Users.filter(username='worker').first()

    return admin, chief, worker
