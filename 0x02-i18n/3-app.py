#!/usr/bin/env python3
"""parameterized templates"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config:
    """ flask config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ determine the best match with our supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ index page route (3-index) """
    return render_template('3-index.html', home_title=gettext("home_title"),
                           home_header=gettext("home_header"))


if __name__ == '__main__':
    app.run(debug=True)
