from flask import Blueprint, jsonify, request
from models import db, People, Favorite
from .people_route import get_all_people

people_bp = Blueprint("people", __name__, url_prefix="/people")
"""
Pendiente el post y get individual
"""


@people_bp.route('/people', methods=['GET'])
def get_all_characters():
    characters = People.query.all()
    list_character = [char.serialize() for char in characters]
    return jsonify(list_character), 200


@people_bp.route('/people', methods=['GET'])
def get_all_characters():
    characters = People.query.all()
    return jsonify([char.serialize() for char in characters]), 200


