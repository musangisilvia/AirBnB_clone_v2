#!/usr/bin/python3
"""
    Script that starts a Flask Web application listening on
    0.0.0.0:5000
"""

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
        function triggered by /hbnb_filters
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()

    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(err):
    storage.close()


if __name__ == '__main__':
    """
        make web page accessible
    """
    app.run(host="0.0.0.0")
