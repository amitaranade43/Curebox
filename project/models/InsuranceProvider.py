from project import db

class InsuranceProvider(db.Model):
    __tablename__ = 'InsuranceProvider'
    package_name = db.Column(db.String(255),primary_key=True)
    package_description = db.Column(db.String(255))
    insurance_duration = db.Column(db.Integer)
    age = db.Column(db.String(255))
    price = db.Column(db.Integer)