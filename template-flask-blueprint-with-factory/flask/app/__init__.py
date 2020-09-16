from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config.config import config

db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)

    @app.route('/')
    def index():
        return 'welcome'

    return app


def register_extensions(app):
    """Register extensions with the Flask application."""
    # flask_sqlalchemy
    db.init_app(app)


def register_blueprints(app):
    """Register blueprints with the Flask application."""
    from .view.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
