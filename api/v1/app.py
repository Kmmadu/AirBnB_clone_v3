#!/usr/bin/python3
"""
AirBnB API: Main entry point for the Flask application
"""

from flask import Flask, jsonify
from flask_cors import CORS
from os import getenv
from api.v1.views import app_views
from models import storage


# Create the Flask application
app = Flask(__name__)

# Configure CORS to allow requests from any origin (for development/testing purposes)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

# Register the blueprint that contains your API routes
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """
    Closes the storage on teardown
    """
    storage.close()

@app.errorhandler(404)
def handle_404(exception):
    """
    Handles 404 errors by returning a JSON response
    """
    data = {
        "error": "Not found"
    }

    resp = jsonify(data)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    # Define the host and port, with default values if not set
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))

    # Run the Flask application
    app.run(host=host, port=port, threaded=True)

