# 引用 flask 內建函式
from flask import Flask, g, request, render_template, abort

# 引用套件
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel

from .config.config import config

db = SQLAlchemy()
babel = Babel()


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_blueprints(app)
    register_extensions(app)
    register_i18n(app)

    return app


def register_blueprints(app):
    """Register blueprints with the Flask application."""
    from .view.index import main
    app.register_blueprint(main, url_prefix='/<lang_code>/main')


def register_extensions(app):
    """Register extensions with the Flask application."""
    babel.init_app(app)
    db.init_app(app)


def register_i18n(app):
    """Register i18n with the Flask application."""
    defalut_language_str = app.config['DEFAULT_LANGUAGE']
    support_language_list = app.config['SUPPORTED_LANGUAGES']

    # 1 Get parameter lang_code from route
    @app.url_value_preprocessor
    def get_lang_code(endpoint, values):
        if values is not None:
            g.lang_code = values.pop('lang_code', defalut_language_str)

    # 2 Check lang_code type is in config
    @app.before_request
    def ensure_lang_support():
        lang_code = g.get('lang_code', None)
        if lang_code and lang_code not in support_language_list:
            g.lang_code = request.accept_languages.best_match(
                support_language_list)

    # 3 Setting babel
    @babel.localeselector
    def get_locale():
        return g.get('lang_code')

    # 4 Check lang_code exist after step1 pop parameter of lang_code
    @app.url_defaults
    def set_language_code(endpoint, values):
        if 'lang_code' in values or not g.lang_code:
            return
        if app.url_map.is_endpoint_expecting(endpoint, 'lang_code'):
            values['lang_code'] = g.lang_code