#!/usr/bin/python3
"""
Blueprint for AirBnB API routes
"""

from flask import Blueprint

# Create a blueprint for version 1 of the API with the URL prefix "/api/v1"
app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")

# Importing individual route modules to ensure they are registered with the blueprint
# Explicit imports help maintain readability and code clarity
from api.v1.views.index import *  # Status endpoint
from api.v1.views.states import *  # State-related endpoints
from api.v1.views.amenities import *  # Amenity-related endpoints
from api.v1.views.cities import *  # City-related endpoints
from api.v1.views.places import *  # Place-related endpoints
from api.v1.views.places_reviews import *  # Place review-related endpoints
from api.v1.views.users import *  # User-related endpoints
from api.v1.views.places_amenities import *  # Place amenity-related endpoints

