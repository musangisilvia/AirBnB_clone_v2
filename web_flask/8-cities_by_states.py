#!/usr/bin/python3
"""
    Script that starts a Flask Web application listening on
    0.0.0.0:5000
"""

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """
        displays a html page containing states
    """
    return render_template('8-cities_by_states.html',
                           states=storage.all("State"))


@app.teardown_appcontext
def teardown(err):
    storage.close()


if __name__ == '__main__':
    """
        make web page accessible
    """
    app.run(host="0.0.0.0")
