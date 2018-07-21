#! ../env/bin/python

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from app.commands import configure_commands
from app.models import db
from app.controllers.main import main
from app.extensions import (
    cache,
    debug_toolbar,
    login_manager
)


def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. app.settings.ProdConfig
    """

    app = Flask(__name__)

    app.config.from_object(object_name)

    # commands
    configure_commands(app)

    # cache
    cache.init_app(app)

    # debug tool bar
    debug_toolbar.init_app(app)

    # SQLAlchemy
    db.init_app(app)
    engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'))
    if not database_exists(engine.url):
        create_database(engine.url)

    # login
    login_manager.init_app(app)

    # register blueprints
    app.register_blueprint(main)

    return app
