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


@people_bp.route('/<int:people_id>', methods=['GET'])
def get_person_by_id(people_id):
    person = People.query.get_or_404(people_id)
    return jsonify(person.serialize()), 200


@people_bp.route('/', methods=['POST'])
def create_person():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    try:
        new_people = People(
            people_name=data.get("name"),
            film_appearance=data.get("film_api"),
            exploded=data.get("exploded"),
            population=data.get("population")
        )

        db.session.add(new_people)
        db.session.commit()
        return jsonify(new_people.serialize()), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500