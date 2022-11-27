from project import db

class Booking(db.Model):
    __tablename__ = 'booking'
    patient_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    fees = db.Column(db.Integer)
    feedback_id = db.Column(db.String(255))
    date = db.Column(db.Date)
    