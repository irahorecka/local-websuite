"""
/irahorecka/__init__.py

Concerns all things irahorecka.com.
"""

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from websuite.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    """Creates Flask application instance."""
    application = Flask(__name__)
    application.config.from_object(config_class)
    CORS(application)
    db.init_app(application)

    from websuite.main.routes import main
    from websuite.errors.handlers import errors

    application.register_blueprint(main)
    application.register_blueprint(errors)

    return application
