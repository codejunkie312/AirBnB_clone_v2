#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Function to print hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Function to print HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """Function to print C"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Function to print python"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
