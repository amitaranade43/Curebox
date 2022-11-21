from project import db

class PatientHistory(db.Model):
    email = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(255))
    #last_name = db.Column(db.String(255))
    age = db.column(db.String(255))
    covid_check = db.Column(db.String(255))
    diseases = db.Column(db.String(255))
    diabetic_check = db.Column(db.String(255))
    vaccinations = db.Column(db.String(255))