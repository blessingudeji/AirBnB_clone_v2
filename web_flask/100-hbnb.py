#!/usr/bin/python3
"""
A script that starts a flask web application
"""
from flask import Flask, render_template, Markup
from models import storage
import sys
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
   """closes the storage session after each request"""    storage.close()


@app.route("/hbnb", strict_slashes=False)
def states_cities_list():
    """
    Displays state and cities if id is given
    """
    states = list(storage.all("State").values())
    states.sort(key=lambda x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    amenities = list(storage.all("Amenity").values())
    amenities.sort(key=lambda x: x.name)
    places = list(storage.all("Place").values())
    places.sort(key=lambda x: x.name)
    for place in places:
        place.description = Markup(place.description)
    return render_template(
        '100-hbnb.html',
        states=states,
        amenities=amenities,
        places=places
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
