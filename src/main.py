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
from models import db, User, Characters, Planets, Favorites, Vehicles

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize erros like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generating sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# User's recovery Database GET
@app.route('/users', methods=['GET'])
def getUsers():
    allUsers = User.query.all()
    allUsers = list(map(lambda x: x.serialize(), allUsers))
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }
    return jsonify(allUsers), 200

# people recovery Database GET List
@app.route('/people', methods=['GET'])
def get_people():
    all_people = Characters.query.all()
    all_people = list(map(lambda x: x.serialize(), all_people))
    return jsonify(all_people), 200

# people  recovery Database GET by ID number
@app.route('/people/<int:char_id>', methods=['GET'])
def get_character(char_id):
    myChar = Characters.query.get(char_id)
    return jsonify(myChar.serialize()), 200

# Planets recovery Database GET List
@app.route('/planets', methods=['GET'])
def get_allplanets():
    allplanets = Planets.query.all()
    allplanets = list(map(lambda x: x.serialize(), allplanets))
    return jsonify(allplanets), 200

# Planets recovery Database GET by ID number
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    myPlanet = Planets.query.get(planet_id)
    return jsonify(myPlanet.serialize()), 200

# Vehicles recovery Database GET List
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    allvehicles = Vehicles.query.all()
    allvehicles = list(map(lambda x: x.serialize(), allvehicles))
    return jsonify(allvehicles), 200

# Posting Add People Favs POST
@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favChar(people_id):
    one = People.query.get(people_id) #busqueda solo por el pk
    user = User.query.get(1)
    if(one):
        new_fav = Fav_people()
        new_fav.email = user.email
        new_fav.people_id = people_id
        db.session.add(new_fav)
        db.session.commit()
        return "Hecho!"
    else:
        raise APIException("no existe el personaje", status_code=404)

#  Posting Planets Add Favs POST
@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favPlanet(planet_id):
    one = Planets.query.get(planets_id) #busqueda solo por el pk
    user = User.query.get(1)
    if(one):
        new_fav = Fav_planets()
        new_fav.email = user.email
        new_fav.planets_id = planets_id
        db.session.add(new_fav)
        db.session.commit()
        return "Hecho!"
    else:
        raise APIException("no existe el personaje", status_code=404)


# Posting Add Vehicles Favs POST
@app.route('/favorite/vehicles/<int:vehicle_id>', methods=['POST'])
def add_favVehicle(vehicle_id):
    one = Vehicles.query.get(planets_id) #busqueda solo por el pk
    user = User.query.get(1)
    if(one):
        new_fav = Fav_vehicles()
        new_fav.email = user.email
        new_fav.vehicles_id = vehicles_id
        db.session.add(new_fav)
        db.session.commit()
        return "Hecho!"
    else:
        raise APIException("no existe el personaje", status_code=404)

# Deleting Planets Favs
@app.GET('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def del_favPlanet(planet_id):
    allFavorites = Favorites.query.all()
    allFavorites = list(map(lambda x: x.serialize(), allFavorites))
    for x in range(len(allFavorites)):
        if allFavorites[x]["Planet ID"] == planet_id:
            idToDelete = allFavorites[x]["ID of this Favorite"]
            Favorites.query.filter_by(id = idToDelete).delete()
            db.session.commit()
            return ("Borré el favorito " + str(allFavorites[x]["ID of this Favorite"]))

# Deleting People Favs
@app.GET('/favorite/people/<int:people_id>', methods=['DELETE'])
def del_favPeople(people_id):
    allFavorites = Favorites.query.all()
    allFavorites = list(map(lambda x: x.serialize(), allFavorites))
    for x in range(len(allFavorites)):
        if allFavorites[x]["Character ID"] == people_id:
            idToDelete = allFavorites[x]["ID of this Favorite"]
            Favorites.query.filter_by(id = idToDelete).delete()
            db.session.commit()
            return ("Borré el favorito " + str(allFavorites[x]["ID of this Favorite"]))
        



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
