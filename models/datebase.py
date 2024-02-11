from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_session, AsyncSession
from sqlalchemy import text, insert
from common import settings_database
from models.schemes import Base

from datetime import time

from models.schemes import (
    TimeClass, DayWeeks, TypeWeek, TokenType, Role
)

from loguru import logger 

engine_async = create_async_engine(
    url=settings_database.db_url_async,
    echo=settings_database.db_debug,
)

async_session_maker = async_sessionmaker(engine_async, expire_on_commit=False)


async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session


def async_db_transaction(engine_async = engine_async):
    """
    Decorator to manage database connection and transaction for an asynchronous function.
    """
    def decorator(func):
        async def wrapper(*args, **kwargs):
            async with engine_async.begin() as conn:
                # Pass the connection object to the decorated function
                await func(conn, *args, **kwargs)
        return wrapper
    return decorator

# Define an asynchronous function to test the database
@async_db_transaction()
async def test_db(conn) -> None:
    rez = await conn.execute(text("SELECT 1"))
    print('tr = ', rez.fetchall())  # Print the result of the query

# Define an asynchronous function to create the database
@async_db_transaction()
async def create_db(conn):
    logger.info('create_db')
    await conn.run_sync(Base.metadata.create_all)

@async_db_transaction()
async def drop_db(conn):
    logger.info('drop_db')
    await conn.run_sync(Base.metadata.drop_all)


class DefaultInsert:
    async def insert_date(data):
        async with async_session_maker() as session:
            session.add_all(data)
            await session.commit()
            logger.info(f'insert_date: {type(data[0])}')

    async def timeclass():
        date = [
            TimeClass(number=1, beginTime=time(9, 20, 0), endTime=time(10, 55, 0)),
            TimeClass(number=2, beginTime=time(11, 5, 0), endTime=time(12, 40, 0)),
            TimeClass(number=3, beginTime=time(13, 20, 0), endTime=time(14, 55, 0)),
            TimeClass(number=4, beginTime=time(15, 5, 0), endTime=time(16, 40, 0))
        ]

        await DefaultInsert.insert_date(data=date)

    async def dayweeks():
        date = [
            DayWeeks(Name='Понедельник', WeekEnd=False),
            DayWeeks(Name='Вторник', WeekEnd=False),
            DayWeeks(Name='Среда', WeekEnd=False),
            DayWeeks(Name='Четверг', WeekEnd=False),
            DayWeeks(Name='Пятница', WeekEnd=False),
            DayWeeks(Name='Суббота', WeekEnd=False),
            DayWeeks(Name='Воскресенье', WeekEnd=True)
        ]
        
        await DefaultInsert.insert_date(data=date)
    
    async def typeweek():
        
        date = [
            TypeWeek(Name='Числитель'),
            TypeWeek(Name='Знаменатель')
        ]
        
        await DefaultInsert.insert_date(data=date)

    async def tokentype():
        date = [
            TokenType(name='Яндекс'),
            TokenType(name='Госуслуги'),
            TokenType(name='Вконтакте'),
            TokenType(name='Телеграм'),
            TokenType(name='Google'),
            TokenType(name='Одноклассники'),
            TokenType(name='Фейсбук'),
            TokenType(name='Инстаграм'),
            TokenType(name='Твиттер')
        ]

        await DefaultInsert.insert_date(data=date)

    async def role():

        date = [
            Role(name='Администратор', level=5),
            Role(name='Редактор', level=2),
            Role(name='Студент', level=0),
            Role(name='SuperUser', level=10)
        ]

        await DefaultInsert.insert_date(data=date)