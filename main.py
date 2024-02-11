from fastapi import FastAPI

from common import settings_api, settings_logger

# TODO: TEST datebase 
from models.datebase import create_db, drop_db, DefaultInsert

import anyio

from routers import router_default, logs_router 

from loguru import logger




def create_app() -> FastAPI:
    app = FastAPI(
        debug= settings_api.debug,
        docs_url='/docs',
        title='SUAI Schedule API(FastAPI)',
    )   

    
    app.include_router(router_default)
    logger.info('include_router(router_default)')

    app.include_router(logs_router)
    logger.info('include_router(logs_router)')

    return app



async def main():
    
    await drop_db()
    await create_db()

    await DefaultInsert.timeclass()
    await DefaultInsert.role()
    await DefaultInsert.typeweek()
    await DefaultInsert.tokentype()
    await DefaultInsert.dayweeks()

if __name__ == '__main__':
    anyio.run(main)
    







