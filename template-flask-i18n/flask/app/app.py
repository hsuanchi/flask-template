from flask import Flask, render_template
from flask_babel import Babel, lazy_gettext, gettext, ngettext, refresh

app = Flask(__name__)
app.config['SECRET_KEY'] = 'development'
app.config['BABEL_DEFAULT_LOCALE'] = 'zh'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

babel = Babel(app)


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
