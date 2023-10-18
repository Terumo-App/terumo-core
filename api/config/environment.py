import os
from functools import lru_cache

from pydantic.v1 import BaseSettings


@lru_cache
def get_env_filename():
    runtime_env = os.getenv('ENV')
    # return f".env.{runtime_env}" if runtime_env else ".env"
    return f'.env.test'


class EnvironmentSettings(BaseSettings):
    APP_NAME: str
    API_VERSION: str
    PUBLIC_KEY: str
    PRIVATE_KEY: str
    HOST: str
    GLOBAL_PROJECT: str

    class Config:
        env_file = get_env_filename()
        env_file_encoding = 'utf-8'


@lru_cache
def get_environment_variables():
    return EnvironmentSettings()
