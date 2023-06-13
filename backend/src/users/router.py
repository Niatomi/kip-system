from src.models import UserOutPydantic
from fastapi.responses import JSONResponse
from tortoise.transactions import in_transaction
from src.utils import check_user_is_not_worker
from tortoise.expressions import Q
from fastapi import status
from fastapi.exceptions import HTTPException
from uuid import UUID
from . import schemas
from fastapi import APIRouter
from fastapi import Depends
from src.auth.oauth2 import get_current_user
from fastapi_pagination import Page
from src.models import UserOutPydantic, Users
from fastapi_pagination.ext.tortoise import paginate

router = APIRouter(prefix='/users',
                   dependencies=[Depends(get_current_user)],
                   tags=['Users'])

roles = ['ADMIN', 'CHIEF', 'WORKER']


@router.get('/', response_model=Page[UserOutPydantic])
async def get_users_pages(role: str = None):

    if role is None:
        return await paginate(Users)
    else:
        try:
            return await paginate(Users.filter(role=role))
        except ValueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Role doesn't exist")


@router.get('/roles')
def get_roles():
    return roles


@router.get('/{user_id}/', response_model=UserOutPydantic)
async def get_user_by_id(user_id: UUID):
    return await Users.filter(id=user_id).first()


@router.get('/user', response_model=UserOutPydantic | None)
async def get_user_by_params(params: schemas.UsersGetParams = Depends(schemas.UsersGetParams)):
    user = await Users.filter(params.expression).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user


@router.post('/', dependencies=[Depends(check_user_is_not_worker)])
async def add_user(sign_up_user: schemas.UserCredentials,
                   signin_user: Users = Depends(get_current_user)):

    if not roles.count(sign_up_user.role):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Role is not presented')

    if signin_user.role == 'CHIEF' and sign_up_user.role == 'ADMIN':
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                            detail='Your basic role is lower than you want to apply to user')

    user = await Users.filter(Q(username=sign_up_user.username) |
                              Q(email=sign_up_user.email)).first()
    if user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User already exists')

    sign_up_user = sign_up_user.dict()
    sign_up_user['password_hash'] = hash(sign_up_user.pop('password'))
    sign_up_user['chief_id'] = signin_user.id

    async with in_transaction():
        await Users.create(**sign_up_user)

    return JSONResponse(status_code=status.HTTP_201_CREATED,
                        content=None)


@router.get('/me',
            response_model=UserOutPydantic)
async def get_current_user(user: Users = Depends(get_current_user)):
    return user
