#!/usr/bin/python3
"""
Defines RESTful API endpoints for managing State objects.
"""

from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_states():
    """
    Retrieves all State objects from storage.

    :return: JSON list of all State objects, HTTP 200 status.
    """
    state_list = [state.to_dict() for state in storage.all(State).values()]
    return jsonify(state_list), 200  # 200 indicates successful retrieval


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state_by_id(state_id):
    """
    Retrieves a specific State object by its ID.

    :param state_id: ID of the State to retrieve.
    :return: JSON of the State object, HTTP 200 on success, HTTP 404 if not found.
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)  # Abort with HTTP 404 if the State is not found

    return jsonify(state.to_dict()), 200  # Return the State data as JSON


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """
    Deletes a specific State object by its ID.

    :param state_id: ID of the State to delete.
    :return: Empty JSON object with HTTP 200 status on success, HTTP 404 if not found.
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)  # Abort with HTTP 404 if the State does not exist

    storage.delete(state)  # Delete the State from storage
    storage.save()  # Persist the deletion
    
    return jsonify({}), 200  # Return HTTP 200 on successful deletion


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """
    Creates a new State object.

    :return: JSON of the newly created State, HTTP 201 status, HTTP 400 if the request is invalid.
    """
    req_json = request.get_json()  # Retrieve JSON data from the request
    if req_json is None:
        abort(400, "Request data is not JSON")  # Abort with HTTP 400 if no JSON data
    
    if 'name' not in req_json:
        abort(400, "Missing 'name' field")  # Abort with HTTP 400 if the 'name' field is missing
    
    state = State(**req_json)  # Create a new State with the provided data
    state.save()  # Save the new State
    
    return jsonify(state.to_dict()), 201  # Return HTTP 201 for successful creation


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """
    Updates a specific State object by its ID.

    :param state_id: ID of the State to update.
    :return: JSON of the updated State, HTTP 200 on success, HTTP 400 for invalid data, HTTP 404 if not found.
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)  # Abort with HTTP 404 if the State does not exist
    
    req_json = request.get_json()  # Retrieve JSON data from the request
    if req_json is None:
        abort(400, "Request data is not JSON")  # Abort with HTTP 400 if no JSON data
    
    # Update allowed fields
    for key, value in req_json.items():
        if key not in ('id', 'created_at', 'updated_at'):  # Ignore protected fields
            setattr(state, key, value)  # Update the State object with new values
    
    state.save()  # Save the updated State
    
    return jsonify(state.to_dict()), 200  # Return HTTP 200 on successful update

