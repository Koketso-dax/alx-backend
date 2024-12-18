#!/usr/bin/env python3
""" A basic flask app with i18n support """
from flask import Flask, g, request, render_template
from flask_babel import Babel, format_datetime
import pytz


class Config:
    """ Representation of babel locale config """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


def get_user():
    """ Retrieve user by id """
    login_id = request.args.get('login_as')

    if login_id:
        return users.get(int(login_id), None)
    return None


@app.before_request
def before_request():
    """login before any request"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Retrieve locale of the user"""
    locale = request.args.get('locale', '')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    header_locale = request.headers.get('locale', '')
    if header_locale and header_locale in app.config['LANGUAGES']:
        return header_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ Retrieve user's timezone """
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


# babel.init_app(app, locale_selector=get_locale,
# timezone_selector=get_timezone)


@app.route('/')
def get_index():
    """ Render index """
    g.time = format_datetime()
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
