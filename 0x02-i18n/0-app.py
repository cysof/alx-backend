#!/usr/bin/env python3
""" Basic Flask Application
"""

from flask import Flask, render_template


# Initializing Flask Application
app = Flask(__name__)

# Define the route for the root URL

@app.route('/')
def index():
    """ Rnder the index.html template"""
    return render_template('0-index.html')

# Main entry to the application
if __name__ == '__main__':
    app.run(debug=True)