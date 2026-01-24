from . import app, mongodb_client
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401
from bson import json_util

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
    count = mongodb_client.picturesdb.pictures.count_documents({})
    return jsonify(length=count), 200

######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    """Return all pictures"""
    result = mongodb_client.picturesdb.pictures.find({})
    return json_util.dumps(list(result)), 200

######################################################################
# GET A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    """Return a specific picture by id"""
    picture = mongodb_client.picturesdb.pictures.find_one({"id": id})
    if picture:
        return json_util.dumps(picture), 200
    return jsonify({"message": "picture not found"}), 404

######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    """Create a new picture"""
    picture_in = request.get_json()
    
    # Check if picture with this id already exists
    picture = mongodb_client.picturesdb.pictures.find_one({"id": picture_in["id"]})
    if picture:
        return jsonify({"Message": f"picture with id {picture_in['id']} already present"}), 302
    
    # Add the new picture to the data list
    mongodb_client.picturesdb.pictures.insert_one(picture_in)
    return json_util.dumps(picture_in), 201

######################################################################
# UPDATE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    """Update an existing picture"""
    picture_in = request.get_json()
    
    # Find and update the picture
    result = mongodb_client.picturesdb.pictures.update_one({"id": id}, {"$set": picture_in})
    if result.matched_count > 0:
        return json_util.dumps(picture_in), 200
    
    # Picture not found
    return jsonify({"message": "picture not found"}), 404

######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    """Delete a picture by id"""
    # Find and delete the picture
    result = mongodb_client.picturesdb.pictures.delete_one({"id": id})
    if result.deleted_count > 0:
        return "", 204
    
    # Picture not found
    return jsonify({"message": "picture not found"}), 404
