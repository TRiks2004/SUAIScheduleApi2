from fastapi import FastAPI

from common.settings import settings_api

# TODO: TEST datebase 
from models.datebase import create_db, drop_db, DefaultInsert

import anyio

def create_app() -> FastAPI:
    app = FastAPI(
        debug= settings_api.debug,
        docs_url='/docs',
        title='SUAI Schedule API(FastAPI)',
    )   

    return app



async def main():
    await drop_db()
    await create_db()

    # await DefaultInsert.timeclass()
    # await DefaultInsert.role()
    # await DefaultInsert.typeweek()
    # await DefaultInsert.tokentype()
    # await DefaultInsert.dayweeks()
    

if __name__ == '__main__':
    anyio.run(main)
    







