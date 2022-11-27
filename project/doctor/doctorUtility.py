from flask import Blueprint, redirect,render_template,request, url_for
from flask_login import login_required, current_user
from project import db
from project.common import commonUtility
from project.models import Doctor, Patient

doctorUtility = Blueprint('doctorUtility', __name__)

@doctorUtility.route('/')
def index():
    return render_template('index.html')


@doctorUtility.route('/doctor/')
@login_required
def doctor():
    return render_template('doctor/doctor.html', name = 'doctor')
  
  
@doctorUtility.route('/searchdoctor',methods=['POST'])
@login_required
def searchdoctor():
    searchquery = request.form.get('searchquery')
    disease = request.form.get('disease')
    covid_care = request.form.get('covid')
    location = request.form.get('location')
    query = commonUtility.getQuery(searchquery,disease,covid_care,location);
    records = db.engine.execute(query)
    diseases = db.engine.execute("select name from disease;")
    locations = db.engine.execute("select distinct h.location from hospital h join doctor d on h.id = d.hospital_id order by 1")
    return render_template('patient/patient.html', name=current_user.name, doctors = records ,diseases = diseases, locations = locations)

