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
    print(records,len(records))
    if len(records)!=0:
        no_of_packages = len(records)
        for i in records:
            revenue_gen = i.revenue
            count = i.people_enrolled
    else:
        revenue_gen=0
        count=0
        no_of_packages=0
    return render_template('insuranceProvider/insuranceProviders.html', name = "insuranceProvider", packages = records,no_of_packages=no_of_packages,no_of_patients=count,Revenue_gen=revenue_gen)

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
    # Insurance_Package = InsuranceProvider(package_name = p_name, package_description = p_description, insurance_duration = i_duration, price= pr, age = a) 
    Insurance_details = InsuranceProvider(package_name=p_name,package_description=p_description,insurance_duration=i_duration,age=a,price=pr)
    db.session.add(Insurance_details)
    db.session.commit()
    return redirect(url_for('insuranceProviderUtility.insuranceProvider'))

@insuranceProviderUtility.route('/suggestInsurance/<string:token>/<string:insurance_id>', methods=['get'])
@login_required
def suggestInsurance(token,insurance_id):
    low = int(token.split('-')[0])
    high = int(token.split('-')[1])
    print(type(low),high)
    str_cmd = "select * from patient where cast(age as int) between "+str(low)+" and "+str(high)+";"
    records_suggest = db.engine.execute(str_cmd).fetchall()
    print("names which are suggested",records_suggest)
    insurance_details= InsuranceProvider.query.filter_by(id=insurance_id).first()
    if records_suggest:
        return render_template('insuranceProvider/suggestInsurance.html', current_user=current_user, name = "insuranceProvider", suggestedNames = records_suggest,insurance_id=insurance_details.id)
    else:
        flash('No Patient in the age range')
        return redirect(url_for('insuranceProviderUtility.insuranceProvider'))

@insuranceProviderUtility.route('/suggestInsurancePatient/<string:token>/<string:insurancePack>', methods=['get'])
@login_required
def suggestInsurancePatient(token,insurancePack):
    print(token)
    insur_id = insurancePack
    update_details = Patient.query.filter_by(id = token).first()
    update_details.insurance_package = insur_id
    db.session.commit()
    return render_template('insuranceProvider/suggestInsurancePatient.html', current_user=current_user, name = "insuranceProvider")




