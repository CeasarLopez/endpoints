"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "User"
    }

    return jsonify(response_body), 200
# # Planets
# # get all planets
@app.route('/Planets', methods=['GET'])
def handle_get_all_planets():
    return "Hello Planets"
# get one planet
@app.route('/planets<int:planet_id', methods=['PUT','GET'])
def handle_get_one_planet(planet_id):
    if request.method == 'GET':
        planet1 = Planets.query.get(planet_id)
        return jsonify(planet1.serialize()), 200
    return "Planet not found", 404
# people
# get all people
@app.route('/people', methods=['GET'])
def handle_get_all_people():
    all_people= People.query.all()
    serialized_people = [person.serialize()for person in all_people]
    return jsonify(serialized_people), 200
# get one person
@app.route('/people<int:person_id>', methods=['PUT','GET'])
def handle_get_one_person(person_id):
    if request.method == 'GET':
        user1 = People.query.get(person_id)
        return jsonify(user1.serialize()), 200
    return "Person not found", 404


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
