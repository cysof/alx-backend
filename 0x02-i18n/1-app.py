#!/usr/bin/env python3

""" Basic Flask app.
Instantiate the Babel object and configure the app to support multiple languages.
Create a Config class with the following attributes:
    LANGUAGES (list): List of supported languages.
    BABEL_DEFAULT_LOCALE (str): Default language for the app.
    BABEL_DEFAULT_TIMEZONE (str): Default timezone for the app.
Define the route for the root URL.
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config(object):
    """
    Configuration class for the application.
        Attributes:
        Languages (list): List of supported languages.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@app.route('/')
def index():
    """ Render the index.html template
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)