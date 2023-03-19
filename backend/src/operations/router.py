from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from database import get_async_session

from pydantic import parse_obj_as

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import insert

from operations.models import Operation
from operations.schema import OperationCreate


from typing import List

router = APIRouter(
    prefix='/operations',
    tags=['operations']
)

@router.get('/get_specific_operation')
async def get_specific_operation(operation_type, session: AsyncSession = Depends(get_async_session)):
    query = select(Operation).where(Operation.type == operation_type)
    result = await session.execute(query)
    return [el[0] for el in result.all()]

@router.post('/insert_operation', status_code=201)
async def add_specific_operation(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    # new_operation_db = Operation(new_operation.from_orm(Operation))
    # print(new_operation_db)
    statement = insert(Operation).values(**new_operation.dict())
    session.add(Operation(**new_operation.dict()))
    
    try:
        await session.commit()
        return 'Data saved'
    except Exception as ex:
        await session.rollback()
        print(ex)