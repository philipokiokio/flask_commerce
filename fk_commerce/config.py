import os

from sqlalchemy.engine.url import URL

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    FLASK_ENV = os.getenv("FLASK_ENV")
    DEBUG = os.getenv("DEBUG")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")
    pass


class DevConfig(Config):
    url_object = URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
    )
    SQLALCHEMY_DATABASE_URI = url_object
    APIFAIRY_TITLE = "FK-Commerce"
    APIFAIRY_UI = "swagger_ui"


class ProdConfig(Config):
    FLASK_ENV = "Production"
    DEBUG = False
    FLASK_DEBUG = False
    pass
    FLASK_DEBUG = False
    pass
