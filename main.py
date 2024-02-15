from contextlib import asynccontextmanager
from fastapi import FastAPI

from common import settings_api

# TODO: TEST datebase 
# from models.datebase import create_db, drop_db, DefaultInsert, InsertShedule

import anyio

from routers import router_default, logs_router, schedule_router 

from loguru import logger

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis


async def init_fast_api_cache():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

async def lifespan(app: FastAPI):
    logger.info('lifespan(app: FastAPI) - startUp')
    ml_models = {}

    await init_fast_api_cache()    
    
    yield ml_models
    logger.info('lifespan(app: FastAPI) - shutdown')


def create_app() -> FastAPI:
    app = FastAPI(
        debug= settings_api.debug,
        docs_url='/docs',
        title='SUAI Schedule API(FastAPI)',
        lifespan=lifespan,
    )   

    
    app.include_router(router_default)
    logger.info('include_router(router_default)')

    app.include_router(logs_router)
    logger.info('include_router(logs_router)')

    app.include_router(schedule_router)
    logger.info('include_router(schedule_router)')

    return app



async def main():
    # await drop_db()
    # await create_db()

    # await DefaultInsert.timeclass()
    # await DefaultInsert.role()
    # await DefaultInsert.typeweek()
    # await DefaultInsert.tokentype()
    # await DefaultInsert.dayweeks()

    # await InsertShedule('tete.json').insert_shedule()
    ...



if __name__ == '__main__':
    anyio.run(main)
    







