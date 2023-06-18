import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = os.getenv("APP_PORT", 8080)


class DevelopmentConfig(Config):
    pass

class StagingConfig(Config):
    pass

class ProductionConfig(Config):
    pass


def get_config():
    env = os.getenv("ENV", "dev")
    config_type = {
        "dev": DevelopmentConfig(),
        "stg": StagingConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
