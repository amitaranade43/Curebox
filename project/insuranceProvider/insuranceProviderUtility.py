from flask import Blueprint, redirect,render_template,request, url_for, flash
from flask_login import login_required, current_user
from project import db
from project.models import InsuranceProvider, Patient
from project.models import User
insuranceProviderUtility = Blueprint('insuranceProviderUtility', __name__)


@insuranceProviderUtility.route('/insuranceProvider')
@login_required
def insuranceProvider():
    records = InsuranceProvider.query.all()
    return render_template('insuranceProvider/insuranceProviders.html', name = "insuranceProvider", packages = records )

@insuranceProviderUtility.route('/createInsurancePackage')
@login_required
def createInsurancePackage():
    return render_template('insuranceProvider/createInsurancePackages.html',  name = "insuranceProvider" )

@insuranceProviderUtility.route('/createInsurancePackage', methods=['POST'])
@login_required
def createInsurancePackage_post():
    p_name = request.form.get('package_name')
    p_description = request.form.get('package_description')
    i_duration = request.form.get('insurance_duration')
    pr = request.form.get('price')
    a = request.form.get('age')
    value= User.query.filter_by(email=current_user.email).first()
    # Insurance_Package = InsuranceProvider(package_name = p_name, package_description = p_description, insurance_duration = i_duration, price= pr, age = a) 
    Insurance_details = InsuranceProvider(package_name=p_name,package_description=p_description,insurance_duration=i_duration,age=a,price=pr)
    db.session.add(Insurance_details)
    db.session.commit()
    records_create = InsuranceProvider.query.all()
    return render_template('insuranceProvider/insuranceProviders.html', current_user=current_user, name = "insuranceProvider", packages = records_create)

@insuranceProviderUtility.route('/suggestInsurance/<string:token>', methods=['get'])
@login_required
def suggestInsurance(token):
    low = int(token.split('-')[0])
    high = int(token.split('-')[1])
    print(type(low),high)
    str_cmd = "select * from patient where cast(age as int) between "+str(low)+" and "+str(high)+";"
    records_suggest = db.engine.execute(str_cmd).fetchall()
    print(records_suggest)
    print("names which are suggested",records_suggest)
    if records_suggest:
        return render_template('insuranceProvider/suggestInsurance.html', current_user=current_user, name = "insuranceProvider", suggestedNames = records_suggest)
    else:
        flash('No Patient in the age range')
        return redirect(url_for('insuranceProviderUtility.insuranceProvider'))

@insuranceProviderUtility.route('/suggestInsurancePatient/<string:token>/<string:isurancePack>', methods=['get'])
@login_required
def suggestInsurancePatient(token,isurancePack):
    print(token)
    insur_id = isurancePack
    update_details = Patient.query.filter_by(id = token).first()
    update_details.insurance_package = insur_id
    db.session.commit()
    return render_template('insuranceProvider/suggestInsurancePatient.html', current_user=current_user, name = "insuranceProvider")
