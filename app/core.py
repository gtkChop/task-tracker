from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from settings import (
    DB_URL,
)

blueprints = (

)


def create_app():
    """
    Create application
    :return:
    """
    application = Flask(__name__)
    application.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app_db = SQLAlchemy(application)
    app_migrate = Migrate(application, app_db)

    for bp in blueprints:
        application.register_blueprint(bp)

    app_db.init_app(application)
    app_migrate.init_app(application, app_db)

    return application, app_db, app_migrate



