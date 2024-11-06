#!/usr/bin/env python3
""" Detect incoming requests containing `locale` """
from flask import Flask, request, render_template
from flask_babel import Babel, gettext


class Config:
    """flask config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
gettext.__doc__ = """ Dynamically assigns texts to html elements """


@babel.localeselector
def get_locale() -> str:
    """get locale from request"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """index page"""
    return render_template('4-index.html', home_title=gettext("home_title"),
                           home_header=gettext("home_header"))


if __name__ == '__main__':
    app.run(debug=True)
