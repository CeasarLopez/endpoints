from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, ForeignKey('planets.id'), nullable=True)
    people_id = db.Column(db.Integer, ForeignKey('people.id'), nullable=True)
    user_id = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "Planets_id": self.Planets_id,
            "People_id" : self.People_id,
            "User_id" : self.User_id
        }

class People(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(120), unique=True, nullable=False)
    Height = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    Favorites= db.relationship("Favorites", backref="People")

    def serialize(self):
        return {
            "id": self.id,
            "Name_id": self.Name_id,
            "Height_id": self.Height_id  
        }
class Planets(db.Model):
    __tablename__ = "planets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.String(80), unique=False, nullable=False)
    population = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    Favorites= db.relationship("Favorites", backref="Planets")

    def serialize(self):
        return {
            "id": self.id,
            "name_id": self.name_id,
            "diameter_id": self.diameter_id,
            "population_id": self.population_id
        }

    def __repr__(self):

        return '<User %r>' % self.username
