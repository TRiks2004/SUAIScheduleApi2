from fastapi import FastAPI

from common import settings_api

# TODO: TEST datebase 
from models.datebase import test_db

import anyio

from routers import include_router

from loguru import logger

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis


async def init_fast_api_cache():
    '''
    init_fast_api_cache()

    Инициализация `FastAPICache` для кэша определённых запросов
    '''
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    logger.info('init_fast_api_cache()')

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

    include_router(app)


    return app



async def main():
    await test_db()
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
    







