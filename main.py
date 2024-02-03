from fastapi import FastAPI

from common.settings import settings_api


def create_app() -> FastAPI:
    app = FastAPI(
        debug= settings_api.debug,
        docs_url='/docs',
        title='SUAI Schedule API(FastAPI)',
    )
    return app





