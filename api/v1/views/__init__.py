#!/usr/bin/python3
"""
Blueprint setup for API v1 views
"""

from flask import Blueprint

# Create a Blueprint for version 1 of the API
app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")

# Import view modules to register their routes with the Blueprint
# Explicit imports are preferred for clarity and to avoid unintended name conflicts
from api.v1.views.index import status, stats
from api.v1.views.states import get_states, get_state, create_state, update_state, delete_state
from api.v1.views.amenities import get_amenities, get_amenity, create_amenity, update_amenity, delete_amenity
from api.v1.views.cities import get_cities, get_city, create_city, update_city, delete_city
from api.v1.views.places import get_places, get_place, create_place, update_place, delete_place
from api.v1.views.places_reviews import get_reviews, get_review, create_review, update_review, delete_review
from api.v1.views.users import get_users, get_user, create_user, update_user, delete_user
from api.v1.views.places_amenities import link_amenity_to_place, unlink_amenity_from_place, get_place_amenities

