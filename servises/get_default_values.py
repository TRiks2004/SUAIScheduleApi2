from models.schemes import(
    TimeClass
)

from sqlalchemy.future import select

from sqlalchemy.ext.asyncio import AsyncSession

from typing import List

async def timeclass_select_all(session: AsyncSession, skip: int = 0, limit: int = 100) -> List[TimeClass]:
    stmt = select(TimeClass).offset(skip).limit(limit)
    
    result = await session.execute(stmt)
    
    return result.scalars().all()

async def timeclass_select_one(session: AsyncSession, number: int) -> TimeClass:
    stmt = select(TimeClass).where(TimeClass.number == number)
    
    result = await session.execute(stmt)
    
    return result.scalars().fetchall()