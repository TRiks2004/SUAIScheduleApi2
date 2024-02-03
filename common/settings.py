from pydantic_settings import BaseSettings

import environ
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

class SettingsAPI(BaseSettings):
    debug: bool = env.bool('DEBUG', default=False)

settings_api = SettingsAPI()

# TODO: Add logers
print(f'{BASE_DIR=}')
print(f'{settings_api.debug=}')