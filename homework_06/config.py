from os import getenv


SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://admin:admin@localhost/hw06",
)

class Config:
    DEBUG = False
    TESTING = False
    ENV = "development"
    SECRET_KEY = "\xa0`\xb7\xf1\xf972hC6\x15\xb6\x1aa\x88\xba5\xceOS&\x9f\xa7\xb8\x00o\xcf%\x81E\xcfC"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI

class ProductionConfig(Config):
    ENV = "production"

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True