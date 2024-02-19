from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.datebase import get_async_session

from sqlalchemy.ext.asyncio import AsyncSession

from models.interface.users import Users

from servises.user import select_user_all

from typing import List

user_router = APIRouter(
    prefix="/user",
    tags=["user"]
)



@user_router.get("/", response_model=List[Users])
async def get_user(
    skip: int = 0, limit: int = 100, 
    session: AsyncSession = Depends(get_async_session)
):
    get = await select_user_all(session, skip, limit)
    return get
