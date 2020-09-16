from flask import Flask, g, request, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel

from .config.config import config

db = SQLAlchemy()
babel = Babel()


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    babel.init_app(app)

    @babel.localeselector
    def get_locale():
        return g.get('lang_code', 'en')

    @app.url_defaults
    def set_language_code(endpoint, values):
        if 'lang_code' in values or not g.get('lang_code', None):
            return
        if app.url_map.is_endpoint_expecting(endpoint, 'lang_code'):
            values['lang_code'] = g.lang_code

    @app.url_value_preprocessor
    def get_lang_code(endpoint, values):
        if values is not None:
            g.lang_code = values.pop('lang_code', None)

    @app.before_request
    def ensure_lang_support():
        lang_code = g.get('lang_code', None)
        if lang_code and lang_code not in app.config[
                'SUPPORTED_LANGUAGES'].keys():
            return abort(404)

    from .view.main import main
    app.register_blueprint(main, url_prefix='/<lang_code>/main')

    return app
