from flask import Blueprint, redirect,render_template,request, url_for
from flask_login import login_required, current_user
from project import db
from project.models import Doctor, Patient

insuranceProviderUtility = Blueprint('insuranceProviderUtility', __name__)


@insuranceProviderUtility.route('/insuranceProvider')
@login_required
def insuranceProvider():
    return render_template('insuranceProvider/insuranceProviders.html', name = 'insuranceprovider')
