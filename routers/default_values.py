from fastapi import APIRouter, Depends
from models.interface.time_class import TimeClass

from datetime import time

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from models.datebase import get_async_session

from servises.get_default_values import timeclass_select_all, timeclass_select_one

from typing import List

router_default = APIRouter(
    prefix="/default",
)


@router_default.get("/timeclass", response_model=List[TimeClass])
async def get_timeclass(
    skip: int = 0, limit: int = 100, 
    session: AsyncSession = Depends(get_async_session)) -> List[TimeClass]:
    
    result = await timeclass_select_all(session, skip, limit)
    print(result) # TODO: Log
    return result

@router_default.get("/timeclass/{number}", response_model=TimeClass)
async def get_timeclass_by_number(
    number: int, 
    session: AsyncSession = Depends(get_async_session)) -> TimeClass:
    
    result = await timeclass_select_one(session, number)
    print(result) # TODO: Log
    return result
