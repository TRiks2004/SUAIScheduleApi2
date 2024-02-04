from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from common.settings import settings_database
from models.Schemes import Base


# Create the asynchronous engine
engine_async = create_async_engine(
    url=settings_database.db_url_async,
    echo=settings_database.db_debug,
)

def async_db_transaction(engine_async):
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
@async_db_transaction(engine_async)
async def test_db(conn) -> None:
    rez = await conn.execute(text("SELECT 1"))
    print('tr = ', rez.fetchall())  # Print the result of the query

# Define an asynchronous function to create the database
@async_db_transaction(engine_async)
async def create_db(conn):
    await conn.run_sync(Base.metadata.create_all)

@async_db_transaction(engine_async)
async def drop_db(conn):
    await conn.run_sync(Base.metadata.drop_all)

