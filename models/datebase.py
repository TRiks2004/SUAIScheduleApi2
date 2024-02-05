from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_session 
from sqlalchemy import text, insert
from common.settings import settings_database
from models.schemes import Base

from datetime import time

from models.schemes import (
    TimeClass, DayWeeks, TypeWeek, TokenType, Role
)

engine_async = create_async_engine(
    url=settings_database.db_url_async,
    echo=settings_database.db_debug,
)

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
    await conn.run_sync(Base.metadata.create_all)

@async_db_transaction()
async def drop_db(conn):
    await conn.run_sync(Base.metadata.drop_all)


class DefaultInsert:

    @async_db_transaction()
    async def insert_date(conn, *, table, data):
        stmt = insert(table).values(data)
        
        await conn.execute(stmt)
        await conn.commit()

    async def timeclass():
        
        date = [{TimeClass.number:1, TimeClass.beginTime:time(9, 20, 0), TimeClass.endTime:time(10, 55, 0)},
                {TimeClass.number:2, TimeClass.beginTime:time(11, 5, 0), TimeClass.endTime:time(12, 40, 0)},
                {TimeClass.number:3, TimeClass.beginTime:time(13, 20, 0), TimeClass.endTime:time(14, 55, 0)},
                {TimeClass.number:4, TimeClass.beginTime:time(15, 5, 0), TimeClass.endTime:time(16, 40, 0)}]

        await DefaultInsert.insert_date(table=TimeClass, data=date)

    async def dayweeks():
        date = [
            {DayWeeks.Name:'Понедельник', DayWeeks.WekEnd:False},
            {DayWeeks.Name:'Вторник', DayWeeks.WekEnd:False},
            {DayWeeks.Name:'Среда', DayWeeks.WekEnd:False},
            {DayWeeks.Name:'Четверг', DayWeeks.WekEnd:False},
            {DayWeeks.Name:'Пятница', DayWeeks.WekEnd:False},
            {DayWeeks.Name:'Суббота', DayWeeks.WekEnd:False},
            {DayWeeks.Name:'Воскресенье', DayWeeks.WekEnd:True},
        ]
        
        await DefaultInsert.insert_date(table=DayWeeks, data=date)
    
    async def typeweek():
        date = [
            {TypeWeek.Name:'Числитель'},
            {TypeWeek.Name:'Знаменатель'},
        ]
        
        await DefaultInsert.insert_date(table=TypeWeek, data=date)

    async def tokentype():
        date = [
            {TokenType.name:'Яндекс'},
            {TokenType.name:'Госуслуги'},
            {TokenType.name:'Вконтакте'},

            {TokenType.name:'Телеграм'},
            {TokenType.name:'Google'},
            {TokenType.name:'Одноклассники'},
            {TokenType.name:'Фейсбук'},
            {TokenType.name:'Инстаграм'},
            {TokenType.name:'Твиттер'},
        ]

        await DefaultInsert.insert_date(table=TokenType, data=date)

    async def role():
        date = [
            {Role.name:'Администратор'},
            {Role.name:'Редактор'},
            {Role.name:'Студент'},
            {Role.name:'SuperUser'},
        ]

        await DefaultInsert.insert_date(table=Role, data=date)