#!/usr/bin/env python3
"""Basic Babel setup with mock login"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    return users.get(int(user_id))


@app.before_request
def before_request():
    user_id = request.args.get('login_as')
    g.user = get_user(user_id) if user_id else None


@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    return render_template('5-index.html', home_title=gettext('home_title'),
                           home_header=gettext('home_header'))


if __name__ == '__main__':
    app.run(debug=True)
