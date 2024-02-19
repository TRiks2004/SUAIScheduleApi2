from .default import router_default
from .log import logs_router
from .schedule import schedule_router
from .user import user_router


from .UserENTER.authentication import auth_router

from loguru import logger

from fastapi import FastAPI


routers = [
    router_default, logs_router, schedule_router, user_router, auth_router
]


def include_router(app: FastAPI):
    '''
    include_router(app: FastAPI)
    
    Подключение роутеров из модулей 'routers'

    Keyword arguments:
        app -- FastAPI

    '''

    for router in routers:
        app.include_router(router)
        logger.info(f'include_router({router.tags})')