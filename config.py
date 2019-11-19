import os


class Config():
    PORT: int = 8080
    HOST: str = "localhost"


class DevConfig(Config):
    DEBUG: bool = True
