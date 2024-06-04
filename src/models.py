from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()
#db.Model = declarative_db.Model()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, unique = True)
    name = db.Column(db.String(250), nullable=True)
    email = db.Column(db.String(250), nullable=False, unique = True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "username": self.username,
        }

class Planets(db.Model):
    __tablename__ = "planets"
    id = db.Column(db.Integer, primary_key=True)
    diameter = db.Column(db.String(30), nullable=False)
    rotation_period = db.Column(db.String(30), nullable=False)
    orbital_period = db.Column(db.String(30), nullable=False)
    gravity = db.Column(db.String(30), nullable=False)
    population = db.Column(db.String(30), nullable=False)
    climate = db.Column(db.String(30), nullable=False)
    terrain = db.Column(db.String(30), nullable=True)
    description = db.Column(db.String(30), nullable=True)
    favorite = db.relationship("Favorites", backref="planets")
    
    def serialize(self):
        return{
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "description": self.description
        }
    
class Vehicles(db.Model):
    __tablename__ = "vehicles"
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), nullable=False)
    vehicle_class = db.Column(db.String(50), nullable=True)
    manufacturer = db.Column(db.String(50), nullable=True)
    cost_in_credits = db.Column(db.String(50), nullable=True)
    length = db.Column(db.String(50), nullable=True)
    crew = db.Column(db.String(50), nullable=True)
    passengers = db.Column(db.String(50), nullable=True)
    favorite = db.relationship("Favorites", backref="vehicles")
    
    def serialize(self):
        return{
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers
        }

class People(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    persons_name = db.Column(db.String(50), nullable=False)
    height = db.Column(db.String(50), nullable=True)
    mass = db.Column(db.String(50), nullable=True)
    hair_color = db.Column(db.String(50), nullable=True)
    skin_color = db.Column(db.String(50), nullable=True)
    eye_color = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(50), nullable=True)
    # planet_id = db.Column(db.Integer, ForeignKey('planets.id'))
    # vehicle_id = db.Column(db.Integer, ForeignKey('vehicles.id'))
    # planet = relationship(Planets)
    # vehicle = relationship(Vehicles)
    favorite = db.relationship("Favorites", backref="people")
    
    def serialize(self):
        return{
            "persons_name": self.persons_name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "gender": self.gender,
            # "planet_id": self.planet_id,
            # "vehicle_id": self.vehicle_id
        }
    
class Favorites(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    person_id = db.Column(db.Integer, ForeignKey('people.id'), nullable=True)
    planet_id = db.Column(db.Integer, ForeignKey('planets.id'), nullable=True)
    vehicle_id = db.Column(db.Integer, ForeignKey('vehicles.id'), nullable=True)

#     user = relationship(User)
#     people = relationship(people)
#     planets = relationship(Planets)
#     vehicles = relationship(Vehicles)

    def serialize(self):
        return{
            "id": self.id,
            "user_id": self.user_id,
            "person_id": self.person_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id
        }