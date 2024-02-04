from sqlalchemy import URL

from pydantic_settings import BaseSettings

import environ
import pathlib

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


settings_api = SettingsAPI()
settings_database = SettingsDatabase()


# TODO: Add logers
print(f'{BASE_DIR=}')

# TODO: Add logers
print(f'{settings_api.model_dump_json()}')

# TODO: Add logers
print(f'{settings_database.model_dump_json()}')
print(f'{settings_database.db_url_async=}')