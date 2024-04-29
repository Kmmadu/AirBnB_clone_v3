#!/usr/bin/python3
"""
API endpoints for status and stats
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage

# Status endpoint
@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """
    Returns the status of the API
    """
    # Create a response with status "OK"
    data = {
        "status": "OK"
    }
    
    # Return the JSON response with a 200 status code
    return jsonify(data), 200


# Stats endpoint
@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def stats():
    """
    Returns the count of various objects in the system
    """
    # Create a dictionary with the count of each object type
    data = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }

    # Return the JSON response with a 200 status code
    return jsonify(data), 200

