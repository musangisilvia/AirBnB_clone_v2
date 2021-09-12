#!/usr/bin/python3
"""
    Script that starts a Flask Web application listening on
    0.0.0.0:5000
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
        function triggered by URL /
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        function triggered by URL /hbnb
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_variable(text):
    """
        function triggered by URL /c/<text>
    """
    txt = text.replace("_", " ")
    return 'C {}'.format(txt)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_var(text='is cool'):
    """
        function triggered by URL /python/(<text>)
    """
    text = text.replace("_", " ")

    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
        function triggered by URL /number/<n>
    """
    if type(n) is int:
        return '{} is a number'.format(n)

if __name__ == '__main__':
    """
        make web page accessible
    """
    app.run(host="0.0.0.0")
