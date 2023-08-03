#!/usr/bin/env python3
"""
flask app
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    Set module variables
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# configuring the flask app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index():
    """
    renders template index.html
    """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
