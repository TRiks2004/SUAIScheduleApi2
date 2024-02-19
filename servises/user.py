import os, sys

from models.schemes import ( 
    Classrooms, Users
)

from models.interface.users import UsersCreate

from sqlalchemy.future import select

from sqlalchemy.ext.asyncio import AsyncSession

from typing import List



async def select_user_all(session: AsyncSession, skip: int = 0, limit: int = 100) -> List[Users]:
    stmt = select(Users).offset(skip).limit(limit)
    result = await session.execute(stmt)

    return result.scalars().all() if (result is not None) else []



async def create_user(user: UsersCreate, session: AsyncSession):
    # new_user = Users(user)
    # session.add(new_user)
    # session.commit()
    # session.refresh(new_user)
    # return new_user

    ...















