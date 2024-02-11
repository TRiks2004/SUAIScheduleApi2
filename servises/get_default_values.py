from models.schemes import(
    TimeClass, DayWeeks, Base, TypeWeek, TokenType, Role
)

from sqlalchemy.future import select

from sqlalchemy.ext.asyncio import AsyncSession

from typing import List, TypeVar

from datetime import date, datetime

T = TypeVar("T")


async def select_all(table, session: AsyncSession, skip: int = 0, limit: int = 100) -> List:
    stmt = select(table).offset(skip).limit(limit)
    result = await session.execute(stmt)

    return result.scalars().all() if (result is not None) else []
     

# ------------------------------------------------------------------------------------------------------------

async def timeclass_select_all(session: AsyncSession, skip: int = 0, limit: int = 100) -> List[TimeClass]:
    return await select_all(TimeClass, session, skip, limit)

async def dayweeks_select_all(session: AsyncSession, skip: int = 0, limit: int = 100) -> List[DayWeeks]:
    return await select_all(DayWeeks, session, skip, limit)

async def typeweek_select_all(session: AsyncSession, skip: int = 0, limit: int = 100) -> List[TypeWeek]:
    return await select_all(TypeWeek, session, skip, limit)

async def tokentype_select_all(session: AsyncSession, skip: int = 0, limit: int = 100) -> List[TokenType]:
    return await select_all(TokenType, session, skip, limit)
    
async def role_select_all(session: AsyncSession, skip: int = 0, limit: int = 100) -> List[Role]:
    return await select_all(Role, session, skip, limit)

# ------------------------------------------------------------------------------------------------------------

async def timeclass_select_one(session: AsyncSession, number: int) -> TimeClass:
    stmt = select(TimeClass).where(TimeClass.number == number)
    result = await session.execute(stmt)
    return result.scalars().fetchall()



async def dayweeks_weekend_select_all(session: AsyncSession, skip: int = 0, limit: int = 100) -> List[DayWeeks]: 
    stmt = select(DayWeeks).where(DayWeeks.WekEnd == True)
    result = await session.execute(stmt)
    
    return result.scalars().all()

async def dayweeks_workday_select_all(session: AsyncSession, skip: int = 0, limit: int = 100) -> List[DayWeeks]: 
    stmt = select(DayWeeks).where(DayWeeks.WekEnd == False)
    result = await session.execute(stmt)
    
    return result.scalars().all()

async def typeweek_auto_select_one(session: AsyncSession, term: str, date_start_term: date) -> TypeWeek:
    stmt = select(TypeWeek).where(TypeWeek.Name == term)
    result = await session.execute(stmt)

    first_row = result.scalars().first()
    
    id = first_row.idTypeWeek

    current_date = datetime.now() 

    difference = (current_date - datetime(date_start_term.year, date_start_term.month, date_start_term.day)).days + 1

    week = int((date_start_term.weekday() + 1 + difference) / 7)

    shift = (id + week) % 2 + 1

    stmt = select(TypeWeek).where(TypeWeek.idTypeWeek == shift)
    result = await session.execute(stmt)

    first_row = result.scalars().first()
        
    return first_row

