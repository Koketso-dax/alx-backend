#!/usr/bin/env python3
""" flask app with lang support & locale """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ get locale """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ index route """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
