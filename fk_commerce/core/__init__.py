import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_marshmallow import Marshmallow
from apifairy import APIFairy


load_dotenv()

database = SQLAlchemy()

db_migration = Migrate()

ma = Marshmallow()

api_fairy = APIFairy()


def create_app(config_type=os.getenv("CONFIG_TYPE")):

    app = Flask(__name__)
    app.config.from_object(config_type)

    initialize_extensions(app=app)
    register_blueprint(app=app)

    return app


def initialize_extensions(app: Flask):

    database.init_app(app)

    import core.models  # noqa: F401

    db_migration.init_app(app=app, db=database)

    ma.init_app(app=app)

    api_fairy.init_app(app=app)


def register_blueprint(app: Flask):
    from core.inventory_api import inventory_category_api_blueprint

    app.register_blueprint(
        blueprint=inventory_category_api_blueprint, url_prefix="/api"
    )
