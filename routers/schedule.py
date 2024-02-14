from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from models.datebase import get_async_session

from typing import List

import json

from servises.get_schedule import (
    select_schedule
)   

schedule_router = APIRouter(
    tags=['Schedule'],
    prefix="/schedule"
)

# , response_model=List[TimeClass]

@schedule_router.get("/{group}/{type_week}")
async def get_timeclass(
    group: str, type_week: str,
    skip: int = 0, limit: int = 100, 
    session: AsyncSession = Depends(get_async_session)):
    get = await select_schedule(type_week, group, session, skip, limit)
    return get