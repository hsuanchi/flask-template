# 引用 Flask 套件
from flask import Flask, abort, render_template, request, jsonify, session, Blueprint

# 引用 SQL 相關模組
from flask_sqlalchemy import SQLAlchemy

# 引用 JWT 相關模組
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,
                                jwt_refresh_token_required,
                                create_refresh_token, get_jwt_identity,
                                fresh_jwt_required)

# 引用其他相關模組
from .config.config import config

db = SQLAlchemy()
jwt = JWTManager()


def create_app(config_name):
    app = Flask(__name__)

    # 設定 config
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app


def register_extensions(app):
    """Register extensions with the Flask application."""
    db.init_app(app)
    jwt.init_app(app)


def register_blueprints(app):
    """Register blueprints with the Flask application."""

    from .view.v1 import api
    app.register_blueprint(api, url_prefix='/v1')
