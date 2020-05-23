# 引用 Flask 套件
from flask import Flask, abort, render_template, request, jsonify, session, Blueprint

# 引用 SQL 相關模組
from flask_sqlalchemy import SQLAlchemy

# 引用其他相關模組
from .config.config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    # 設定 config
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)

    @app.route('/')
    def index():
        return 'success'

    @app.route('/create_all')
    def create_db():
        db.create_all()
        return 'success'

    # 判斷權限需要 normal 以上
    @app.route('/normal_member')
    @check_login('normal')
    def member_normal_page():
        name = session.get('username')
        role = session.get('role')
        uid = session.get('uid')
        return f'type:nornal,{name},{role},{uid}'

    # 判斷權限需要 admin 以上
    @app.route('/admin_member')
    @check_login('admin')
    def member_admin_page():
        name = session.get('username')
        role = session.get('role')
        uid = session.get('uid')
        return f'type:admin,{name},{role},{uid}'

    return app


def register_extensions(app):
    """Register extensions with the Flask application."""
    db.init_app(app)


def register_blueprints(app):
    """Register blueprints with the Flask application."""
    from .view.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')


def check_login(check_role):
    def decorator(func):
        def wrap(*args, **kw):
            user_role = session.get('role')
            print(user_role)
            print(type(user_role))

            if user_role == None or user_role == '':
                return abort(401)
            else:
                if check_role == 'admin' and check_role == user_role:
                    return func(*args, **kw)
                if check_role == 'normal':
                    return func(*args, **kw)
                else:
                    return abort(401)

        wrap.__name__ = func.__name__
        return wrap

    return decorator
