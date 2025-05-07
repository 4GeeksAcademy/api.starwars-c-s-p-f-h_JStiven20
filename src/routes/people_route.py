from flask import Blueprint, jsonify, request
from models import db, People, Favorite
from .people_route import get_all_people

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("/", methods=["GET"])
def get_all_planets():
    list_planets = Planet.get_planets(False)
    return jsonify(list_planets)

@planets_bp.route("/", methods=["POST"])
def create_planet():
    data_request = request.get_json()
    if not "planet_name" in data_request or not "population" in data_request:
        return jsonify({"error": "Los siguientes campos son requeridos"})

    planet_id = data_request["planet_id"]
    planet = Planet.query.get_or_404(planet_id)

    new_planet = Planet(
        planet_name=data_request["name"],
        film_appearance=data_request["film_api"],
        exploded=data_request["exploded"],
        population=data_request["population"]
    )
