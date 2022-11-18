from flask import Blueprint, redirect,render_template,request, url_for
from flask_login import login_required, current_user
from . import db
from .models import Patient, PatientHistory

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')



@main.route('/updatepatient')
@login_required
def updatepatient():
    return render_template('update_patient.html', name=current_user.name)


@main.route('/updatepatient',methods=['POST'])
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

    return render_template('patient.html', current_user=current_user)





@main.route('/doctor/')
@login_required
def doctor():
    return render_template('doctor.html', current_user=current_user)

@main.route('/patient/')
@login_required
def patient():
    return render_template('patient.html', current_user=current_user)

@main.route('/insuranceProvider')
@login_required
def insuranceProvider():
    return render_template('insuranceProviders.html', current_user=current_user)


# @main.route('/updateProfile/')
# @login_required
# def account_dets_patient():
#     return render_template('profile_deva.html',current_user=current_user)

# @main.route('/updateProfile/',methods=['POST'])
# @login_required
# def account_dets_patient_post():

#     email = current_user.email
#     username = current_user.username
#     #last_name = current_user.last_name
#     age = request.form.get('age')
#     covid_check = request.form.get('covid_check')
#     diseases = request.form.get('diseases')
#     diabetic_check = request.form.get('diabetic_check')
#     vaccinations = request.form.get('vaccinations')

#     Patient_History = PatientHistory(email=email, username=username,age=age,covid_check=covid_check,diseases=diseases,diabetic_check=diabetic_check,vaccinations=vaccinations) 

#     db.session.add(Patient_History)
#     db.session.commit()

    
#     return redirect(url_for('main.patient'))




