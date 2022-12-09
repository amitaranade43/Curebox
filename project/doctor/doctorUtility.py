from flask import Blueprint, redirect,render_template,request, url_for
from flask_login import login_required, current_user
from project import db
from project.common import commonUtility
from project.models import Patient, User , Booking

doctorUtility = Blueprint('doctorUtility', __name__)

@doctorUtility.route('/')
def index():
    return render_template('index.html')


@doctorUtility.route('/doctor/')
@login_required
def doctor():
    doctor_id = str(current_user.id)
    query = "select pt.firstname,pt.lastname,b.date,b.start_time,b.end_time,b.patient_id from booking b join patient pt on b.patient_id = pt.id where b.status='OPEN' and b.doctor_id = "+ doctor_id +" order by b.start_time;"
    records = db.engine.execute(query)
    return render_template('doctor/doctor.html', name=current_user.first_name ,appointments = records)
  
  
@doctorUtility.route('/searchdoctor',methods=['POST'])
@login_required
def searchdoctor():
    searchquery = request.form.get('searchquery')
    disease = request.form.get('disease')
    covid_care = request.form.get('covid')
    location = request.form.get('location')
    query = commonUtility.getQuery(searchquery,disease,covid_care,location)
    records = db.engine.execute(query)
    print(records)
    diseases = db.engine.execute("select name from disease;")
    locations = db.engine.execute("select distinct h.location from hospital h join doctor d on h.id = d.hospital_id order by 1")
    return render_template('patient/patient.html', name=current_user.first_name, doctors = records ,diseases = diseases, locations = locations)


@doctorUtility.route('/completeAppointment/<string:patientId>',methods=['GET','POST'])
@login_required
def completeAppointment(patientId : str):
    patient = Patient.query.filter_by(id = patientId).first()
    return render_template('doctor/completeAppointment.html', patient=patient)


@doctorUtility.route('/markAsCompleteAppointment/<string:patientId>',methods=['POST'])
@login_required
def markAsCompleteAppointment(patientId : str):

    doctor = User.query.filter_by(email=current_user.email).first()
    print('doctor id is ', doctor.id)
    print('patient id is ', patientId)

    update_booking = Booking.query.filter_by(patient_id = patientId , doctor_id = doctor.id).first()

    update_booking.status = 'COMPLETE'
    db.session.commit()

    # updateQuery = "update booking set status='OPEN' where patient_id = "+ str(patientId) + "  and doctor_id = "+ str(doctor.id) +" ;"
    # db.engine.execute(updateQuery)
    query = "select pt.firstname,pt.lastname,b.date,b.start_time,b.end_time,b.patient_id from booking b join patient pt on b.patient_id = pt.id where b.status='OPEN' order by b.start_time;"
    records = db.engine.execute(query)
    return render_template('doctor/doctor.html', name=current_user.first_name ,appointments = records)
  
    

    
    
