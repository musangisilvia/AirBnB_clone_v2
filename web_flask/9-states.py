#!/usr/bin/python3
"""
    Script that starts a Flask Web application listening on
    0.0.0.0:5000
"""

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
        displays a html page containing states
    """
    return render_template('9-states.html',
                           states=storage.all("State"))


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """
        displays state based on id passed
    """
    states = storage.all("State")
    state = ''
    for state_id in states:
        if state_id == id:
            state = states[state_id]
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown(err):
    storage.close()


if __name__ == '__main__':
    """
        make web page accessible
    """
    app.run(host="0.0.0.0")
