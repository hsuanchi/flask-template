from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config.config import config

db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    @app.route('/')
    def index():
        return 'welcome'

    return app
