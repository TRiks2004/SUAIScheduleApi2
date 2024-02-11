from sqlalchemy import URL

from pydantic_settings import BaseSettings

import environ
import pathlib

from loguru import logger


BASE_DIR = pathlib.Path(__file__).parent.parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

class SettingsAPI(BaseSettings):
    debug: bool = env.bool('DEBUG_API', default=False)

class SettingsDatabase(BaseSettings):
    db_name: str = env.str('DB_NAME')
    db_host: str = env.str('DB_HOST')
    db_port: int = env.int('DB_PORT')
    db_user: str = env.str('DB_USER')
    db_password: str = env.str('DB_PASSWORD')
    db_debug: bool = env.bool('DB_DEBUG', default=False)

    @property
    def db_url_async(self) -> URL:

        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
        )





class SettingsLogger(BaseSettings):
    sink: str = 'logger/log/log.json'
    format_log: str = '{elapsed} | {time:DD.MM.YYYY HH:mm:ss.SSSZ} | {level} | {message} | {file} | {module}:{function}:{line}'
    level: str = 'DEBUG'
    rotation: str = '00:00'
    compression: str = 'zip'
    serialize: bool = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_logger_options()

    def add_logger_options(self) -> None:
        logger.add(
            sink=self.sink,
            format=self.format_log,
            level=self.level,
            rotation=self.rotation,
            compression=self.compression,
            serialize=self.serialize,
            delay=True
        )




settings_api = SettingsAPI()
settings_database = SettingsDatabase()
settings_logger = SettingsLogger()


# TODO: Add logers
print(f'{BASE_DIR=}')

# TODO: Add logers
print(f'{settings_api.model_dump_json()}')

# TODO: Add logers
print(f'{settings_database.model_dump_json()}')
print(f'{settings_database.db_url_async=}')