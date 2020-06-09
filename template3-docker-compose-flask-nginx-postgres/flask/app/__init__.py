from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config.config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    # 設定config
    app.config.from_object(config['development'])

    db.init_app(app)

    from .models.users import Person

    @app.route('/')
    def index():
        return 'hello world'

    @app.route('/create')
    def create_db():
        db.create_all()
        return 'ok'

    @app.route('/max')
    def insert_max():
        u = Person('Max')
        db.session.add(u)
        db.session.commit()
        return 'ok'

    return app