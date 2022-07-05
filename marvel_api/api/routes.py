from flask import Blueprint, request, jsonify
from marvel_api.helpers import token_required
from marvel_api.models import db, User, SuperHero, superhero_schema, superheros_schema

api = Blueprint('api', __name__, url_prefix = '/api')

# CREATE hero ENDPOINT
@api.route('/heros', methods = ['POST'])
@token_required
def create_superhero(current_user_token):
    name = request.json['name']
    description = request.json['description']
    comics_appeared_in = request.json['comics_appeared_in']
    super_power = request.json['super_power']
    user_token = current_user_token.token

    print(f"BIG TESTER: {current_user_token.token}")

    superhero = SuperHero(name, description, comics_appeared_in, super_power, user_token = user_token  )

    db.session.add(superhero)
    db.session.commit()

    response = superhero_schema.dump(superhero)

    return jsonify(response)

# Retrieve all hero Endpoints
@api.route('/heros', methods = ['GET'])
@token_required
def get_superheros(current_user_token):
    owner = current_user_token.token
    superheros = SuperHero.query.filter_by(user_token = owner).all()
    response = superheros_schema.dump(superheros)
    return jsonify(response)


# Retrieve ONE hero Endpoint
@api.route('/heros/<id>', methods = ['GET'])
@token_required
def get_superhero(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        superhero = SuperHero.query.get(id)
        response = superhero_schema.dump(superhero)
        return jsonify(response)
    else:
        return jsonify({'message': "Valid Token Required"}), 401

# Update hero
@api.route('/heros/<id>', methods = ['POST', 'PUT'])
@token_required
def update_superhero(current_user_token, id):
    superhero = SuperHero.query.get(id)

    SuperHero.name = request.json['name']
    SuperHero.description = request.json['description']
    SuperHero.comics_appeared_in = request.json['comics_appeared_in']
    SuperHero.super_power = request.json['super_power']
    SuperHero.user_token = current_user_token.token

    db.session.commit()
    response = SuperHero.dump(superhero)
    return jsonify(response)

# Delete hero
@api.route('/heros/<id>', methods=['DELETE'])
@token_required
def delete_superhero(current_user_token, id):
    superhero = SuperHero.query.get(id)
    db.session.delete(superhero)
    db.session.commit()
    response = superhero_schema.dump(superhero)
    return jsonify(response)