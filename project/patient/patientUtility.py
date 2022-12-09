from flask import Blueprint, redirect,render_template,request
from flask_login import login_required, current_user
from project import db
from project.models import Patient
from flask import Blueprint, redirect,render_template,request, url_for, flash, send_file, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user
from project import db
from project.models import Patient, Doctor, Booking
from project.models import User
import base64
from base64 import b64encode
from io import BytesIO
from werkzeug.utils import secure_filename
import uuid as uuid
import os


patientUtility = Blueprint('patientUtility', __name__)

@patientUtility.route('/updatepatient')
@login_required
def updatepatient():
    patient_details = Patient.query.filter_by(email = current_user.email).first()
    return render_template('patient/update_patient.html', name= 'patient', patient = patient_details)


@patientUtility.route('/updatepatient',methods=['GET','POST'])
@login_required
def updatepatient_post():
    
    if "post":
        #code to insert patient details into database
        fname = request.form.get('firstname')
        lname = request.form.get('lastname')
        email_id = request.form.get('email')
        ag = str(request.form.get('age'))
        gen = request.form.get('gender')
        wt = str(request.form.get('weight'))
        ht = str(request.form.get('height'))
        illness = request.form.get('illness')
        profile_picture = request.files.get('inputFile')
        saver = request.files.get('inputFile')
        profile_picname = secure_filename(profile_picture.filename)
        pic_name = str(uuid.uuid1()) + "_" + profile_picname
        profile_picture = pic_name
        

        #print(fname, lname, ag, gen, wt, ht, illness)
        value= User.query.filter_by(email=current_user.email).first()
        print(value.first_name,value.last_name)
        patient_details = Patient.query.filter_by(email = current_user.email).first()
        if(patient_details is None):
            record = Patient(id=value.id, firstname=fname, lastname=lname, email = email_id, age= ag, gender=gen, weight=wt, height=ht, currentillness=illness, profile_picture=profile_picture)
            db.session.add(record)
            db.session.commit()
            saver.save(os.path.join(current_app.config['UPLOAD_FOLDER'],pic_name))
            
        else:
            #code to update the data in database
            update_details = Patient.query.filter_by(email = value.email).first()
            update_details.firstname = request.form.get('firstname')
            update_details.lastname = request.form.get('lastname')
            update_details.age = str(request.form.get('age'))
            update_details.gender = request.form.get('gender')
            update_details.weight = str(request.form.get('weight'))
            update_details.height = str(request.form.get('height'))
            update_details.currentillness = request.form.get('illness')
            update_details.profile_picture = request.files.get('inputFile')

            saver = request.files.get('inputFile')
            profile_picname = secure_filename(update_details.profile_picture.filename)
            pic_name = str(uuid.uuid1()) + "_" + profile_picname
            update_details.profile_picture = pic_name
            db.session.commit()
            saver.save(os.path.join(current_app.config['UPLOAD_FOLDER'], pic_name))

        patient_details = Patient.query.filter_by(email = current_user.email).first()   
        return render_template('patient/update_patient.html', name= 'patient', patient = patient_details) 

# @patientUtility.route('/patient')
# @login_required
# def patient():
#     records = db.engine.execute("select d.fees , u.name from doctor d natural join curebox_user u ;")
#     return render_template('patient/patient.html', name=current_user.name, doctors = records)

@patientUtility.route('/patient')
@login_required
def patient():
    print('Currently in patient')
    records = db.engine.execute("select d.fees , u.first_name,u.last_name from doctor d natural join public.user u ;")
    print('After records')
    diseases = db.engine.execute("select name from disease;")
    locations = db.engine.execute("select distinct h.location from hospital h join doctor d on h.id = d.hospital_id order by 1")
    return render_template('patient/patient.html', name='patient', doctors = records ,diseases = diseases, locations = locations)

@patientUtility.route('/bookAppointment/')
@login_required
def book_appointment():
    doctors = Doctor.query.all()
    for doc in doctors:
        print(doc.name)
    return render_template('patient/bookAppointment.html',current_user=current_user,doctors_list = doctors)
 
@patientUtility.route('/bookAppointment/', methods=['POST'])
@login_required
def bookAppointment():
    print('Hi')
    userid = current_user.id
    apt_date = request.form.get("Appointment_date")
    doctor_name = request.form.get("doctor_name")
    print(doctor_name)
    print(apt_date)
    doctor = Doctor.query.filter_by(name = doctor_name).first()
    print(doctor.id)
    bookings = Booking.query.filter_by(doctor_id = doctor.id,date = apt_date).first()
    print(bookings)
    return render_template('patient/bookAppointment.html',booked_slots = bookings)
