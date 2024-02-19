from fastapi import APIRouter, Depends

from fastapi_cache.decorator import cache

from models.interface.time_class import TimeClass
from models.interface.day_weeks import DayWeeks
from models.interface.type_week import TypeWeek
from models.interface.token_type import TokenType
from models.interface.role import Role

from datetime import date

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from models.datebase import get_async_session

from servises.get_default_values import (
    timeclass_select_all, timeclass_select_one, 
    dayweeks_select_all, dayweeks_weekend_select_all, 
    dayweeks_workday_select_all, typeweek_select_all,
    typeweek_auto_select_one, tokentype_select_all,
    role_select_all
)

import time

from typing import List

router_default = APIRouter(
    prefix="/default",
)

# timeclass
# ----------------------------------------------------------------------------------------------------------------

@router_default.get("/timeclass", response_model=List[TimeClass])
@cache(expire=120)
async def get_timeclass(
    skip: int = 0, limit: int = 100, 
    session: AsyncSession = Depends(get_async_session)) -> List[TimeClass]:
    # TODO: Log
    return await timeclass_select_all(session, skip, limit)
    

@router_default.get("/timeclass/{number}", response_model=TimeClass)
@cache(expire=120)
async def get_timeclass_by_number(
    number: int, 
    session: AsyncSession = Depends(get_async_session)) -> TimeClass:
    # TODO: Log
    return await timeclass_select_one(session, number)

# dayweeks
# ----------------------------------------------------------------------------------------------------------------

@router_default.get("/dayweeks", response_model=List[DayWeeks])
@cache(expire=120)
async def get_dayweeks(
    skip: int = 0, limit: int = 100, 
    session: AsyncSession = Depends(get_async_session)) -> List[DayWeeks]:
    # TODO: Log
    return await dayweeks_select_all(session, skip, limit)


@router_default.get("/dayweeks/weekend", response_model=List[DayWeeks])
@cache(expire=120)
async def get_dayweeks_weekend(
    skip: int = 0, limit: int = 100, 
    session: AsyncSession = Depends(get_async_session)) -> List[DayWeeks]:
    # TODO: Log
    return await dayweeks_weekend_select_all(session, skip, limit)


@router_default.get("/dayweeks/workday", response_model=List[DayWeeks])
@cache(expire=120)
async def get_dayweeks_workday(
    skip: int = 0, limit: int = 100, 
    session: AsyncSession = Depends(get_async_session)) -> List[DayWeeks]:
    # TODO: Log
    return await dayweeks_workday_select_all(session, skip, limit)

# typeweek
# ----------------------------------------------------------------------------------------------------------------

@router_default.get("/typeweek", response_model=List[TypeWeek])
@cache(expire=120)
async def get_typeweek(
    skip: int = 0, limit: int = 100, 
    session: AsyncSession = Depends(get_async_session)) -> List[TypeWeek]:
    # TODO: Log
    return await typeweek_select_all(session, skip, limit)

@router_default.get("/typeweek/auto", response_model=TypeWeek)
@cache(expire=120)
async def get_typeweek_auto(
    term: str, date_start_term: date,
    session: AsyncSession = Depends(get_async_session)) -> TypeWeek:
    # TODO: Log
    return await typeweek_auto_select_one(session, term, date_start_term)
    
# tokentype
# ----------------------------------------------------------------------------------------------------------------

@router_default.get("/tokentype", response_model=List[TokenType])
@cache(expire=120)
async def get_tokentype(
    skip: int = 0, limit: int = 100, 
    session: AsyncSession = Depends(get_async_session)) -> List[TokenType]:
    # TODO: Log
    return await tokentype_select_all(session, skip, limit)

# role
# ----------------------------------------------------------------------------------------------------------------

@router_default.get("/role", response_model=List[Role])
@cache(expire=120)
async def get_role(
    skip: int = 0, limit: int = 100, 
    session: AsyncSession = Depends(get_async_session)) -> List[Role]:
    # TODO: Log
    return await role_select_all(session, skip, limit)





