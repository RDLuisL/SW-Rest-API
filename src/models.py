from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Defining User Class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }

# Defining Characters Class
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    charName = db.Column(db.String(120), unique=True nullable=False)
    charBirthYear = db.Column(db.String(15), unique=False nullable=True)
    charGender = db.Column(db.String(15), unique=False nullable=True)
    charHairColor = db.Column(db.String(15), unique=False nullable=True)
    charEyeColor = db.Column(db.String(15), unique=False nullable=True)
    charRel = db.relationship("Favorites")

    def __repr__(self):
        return '<Character %r>' % self.charName
    
    def serialize(self):
        return {
            "id": self.id,
            "Name": self.charName,
            "Birth_Year": self.charBirthYear,
            "Gender": self.charGender,
            "Hair_Color": self.charHairColor,
            "Eye_Color": self.charEyeColor,
        }




# Defining Planets Class
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planetsName = db.Column(db.String(120), unique=True nullable=False)
    planetsClimate = db.Column(db.String(15), unique=False nullable=False)
    planetsDiameter = db.Column(db.Integer, unique=True nullable=False)
    planetsPopulation = db.Column(db.Integer, unique=True nullable=False)
    planetsrel = db.relationship("Favorites")

    def __repr__(self):
        return '<planets %r>' % self.planetName

    def serialize(self):
        return {
            "id": self.id,
            "Name": self.planetName,
            "Climate": self.planetClimate,
            "Diameter": self.planetDiameter,
            "Population": self.planetPopulation
        }

# Defining Vehicles Class
class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargoCapacity = db.Column(db.Integer, unique=True nullable=False)
    consumables = db.Column(db.Integer, unique=False nullable=False)
    costInCredits = db.Column(db.Integer, unique=False nullable=False)
    crew = db.Column(db.Integer, unique=False nullable=False)
    manufacturer = db.Column(db.String(30), unique=False nullable=False)
    maxSpeed = db.Column(db.Integer, unique=False nullable=False)
    model = db.Column(db.String(30), unique=True nullable=False)
    passengers = db.Column(db.Integer, unique=False nullable=False)
    vehicleRel = db.relationship("Favorites")

    def __repr__(self):
        return '<vehicles %r>' % self.model

    def serialize(self):
        return {
            "id": self.id,
            "Cargo_Capacity": self.cargoCapacity,
            "Consumables": self.consumables,
            "Cost_In_Credits": self.costInCredits,
            "Crew": self.crew,
            "Manufacturer": self.manufacturer,
            "Max_Speed": self.maxSpeed,
            "Model": self.model,
            "Passengers": self.passengers,
        }

# Defining Favorite Class
class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("user.id"), unique=False nullable=False)
    charId = db.Column(db.Integer, db.ForeignKey("characters.id"), unique=False nullable=True)
    vehicleId = db.Column(db.Integer, db.ForeignKey("vehicles.id"), unique=False nullable=True)
    planetId = db.Column(db.Integer, db.ForeignKey("planets.id"), unique=False nullable=True)

    def __repr__(self):
        return '<favorites %r>' % self.id

    def serialize(self):
        return {
            "ID_of_this_Favorite": self.id,
            "Favorite_of_User": self.userId,
            "Character_ID": self.charId,
            "Vehicle_ID": self.vehicleId,
            "Planets_ID": self.planetId
        }