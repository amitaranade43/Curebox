from . import db
from flask_login import UserMixin
from . import db

class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    rolename = db.Column(db.String(255), unique=True)

#patient table
#forienkey to refer user table
#forienkry for iinsurance

#insurance table
#disease table- descriptions of diseas
#patient disease table - foreign key to user, disease


    
class Patient(db.Model):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    age = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    weight = db.Column(db.String(255))
    height = db.Column(db.String(255))
    currentillness = db.Column(db.String(255))
    pastillness = db.Column(db.String(255))

class PatientHistory(db.Model):
    email = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(255))
    #last_name = db.Column(db.String(255))
    age = db.column(db.String(255))
    covid_check = db.Column(db.String(255))
    diseases = db.Column(db.String(255))
    diabetic_check = db.Column(db.String(255))
    vaccinations = db.Column(db.String(255))

class Disease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),unique=True)