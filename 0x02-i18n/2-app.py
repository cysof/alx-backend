#!/usr/bin/env python3
""" Basic Flask app.
Instantiate the Babel object and configure the app to support
multiple languages.
Create a Config class with the following attributes:
    LANGUAGES (list): List of supported languages.
    BABEL_DEFAULT_LOCALE (str): Default language for the app.
    BABEL_DEFAULT_TIMEZONE (str): Default timezone for the app.
Define the route for the root URL.
Create a get_locale function with the babel.localeselector decorator.
Use request.accept_languages to determine the best match
with our supported languages.
"""

from flask import Flask, render_template
from flask_babel import Babel
from flask import request

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

@babel.localeselector
def get_locale():
        """
        Returns the best matching language from the list of supported languages based on the client's accepted languages.

        :return: The best matching language from the list of supported languages.
        :rtype: str
        """
        return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """ Render the index.html template
    """
    return render_template('2-index.html')


if __name__ == "__main__":
     app.run(debug=True)
     
