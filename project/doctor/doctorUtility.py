from flask import Blueprint, redirect,render_template,request, url_for
from flask_login import login_required, current_user
from project import db
from project.models import Patient, PatientHistory

doctorUtility = Blueprint('doctorUtility', __name__)

@doctorUtility.route('/')
def index():
    return render_template('index.html')


@doctorUtility.route('/doctor/')
@login_required
def doctor():
    return render_template('doctor/doctor.html', current_user=current_user)
