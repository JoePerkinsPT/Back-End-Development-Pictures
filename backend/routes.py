from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))

######################################################################
# RETURN HEALTH OF THE APP
######################################################################


@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################


@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200

    return {"message": "Internal server error"}, 500


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    """Return all pictures"""
    return jsonify(data), 200

######################################################################
# GET A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    """Return a specific picture by id"""
    for picture in data:
        if picture["id"] == id:
            return jsonify(picture), 200
    return jsonify({"message": "picture not found"}), 404


######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    """Create a new picture"""
    picture_in = request.get_json()
    
    # Check if picture with this id already exists
    for picture in data:
        if picture["id"] == picture_in["id"]:
            return jsonify({"Message": f"picture with id {picture_in['id']} already present"}), 302
    
    # Add the new picture to the data list
    data.append(picture_in)
    return jsonify(picture_in), 201

######################################################################
# UPDATE A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    """Update an existing picture"""
    picture_in = request.get_json()
    
    # Find and update the picture
    for i, picture in enumerate(data):
        if picture["id"] == id:
            data[i] = picture_in
            return jsonify(picture_in), 200
    
    # Picture not found
    return jsonify({"message": "picture not found"}), 404

######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    """Delete a picture by id"""
    # Find and delete the picture
    for i, picture in enumerate(data):
        if picture["id"] == id:
            data.pop(i)
            return "", 204
    
    # Picture not found
    return jsonify({"message": "picture not found"}), 404
