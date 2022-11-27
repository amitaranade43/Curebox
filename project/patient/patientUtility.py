from flask import Blueprint, redirect,render_template,request
from flask_login import login_required, current_user
from project import db
from project.models import Patient

patientUtility = Blueprint('patientUtility', __name__)

@patientUtility.route('/updatepatient')
@login_required
def updatepatient():
    return render_template('patient/update_patient.html', name=current_user.name)


@patientUtility.route('/updatepatient',methods=['POST'])
@login_required
def updatepatient_post():
    #code to insert patient details into database
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    age = request.form.get('age')
    gender = request.form.get('gender')
    weight = request.form.get('weight')
    height = request.form.get('height')
    currentillness = request.form.get('currentillness')
    pastillness = request.form.get('pastillness')

    Patient_profile = Patient(firstname=firstname, lastname=lastname, age=age, gender= gender, weight=weight, height=height, currentillness= currentillness, pastillness= pastillness) 

    db.session.add(Patient_profile)
    db.session.commit

    return render_template('patient/patient.html', current_user=current_user)






@patientUtility.route('/patient')
@login_required
def patient():
    records = db.engine.execute("select d.fees , u.name from doctor d natural join curebox_user u ;")
    diseases = db.engine.execute("select name from disease;")
    locations = db.engine.execute("select distinct h.location from hospital h join doctor d on h.id = d.hospital_id order by 1")
    return render_template('patient/patient.html', name=current_user.name, doctors = records ,diseases = diseases, locations = locations)