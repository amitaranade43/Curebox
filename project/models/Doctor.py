from project import db

class Doctor(db.Model):
    __tablename__ = 'doctor'
    id = db.Column(db.Integer, db.ForeignKey('curebox_user.id'), primary_key=True)
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'))
    fees = db.Column(db.Integer)
    provide_covid_care = db.Column(db.Boolean)
    name = db.Column(db.String(255))
    # doctorAvailability = db.relationship('DoctorAvailability', backref='doctor')
    booking = db.relationship('Booking', backref='doctor')
