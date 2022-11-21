from flask import Blueprint,render_template,redirect, url_for,flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from project.models import User
from project import db
from flask_login import login_user, login_required, logout_user
from threading import Thread


routes = Blueprint('routes', __name__)


@routes.route('/login')
def login():
    return render_template('login.html')

@routes.route('/signup')
def signup():
    return render_template('signup.html')

@routes.route('/signup', methods=['GET','POST'])
def signup_post():
    if "post":
        # code to validate and add user to database goes here
        email = request.form.get('email')
        print(email)
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        if user: # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address already exists')
            return redirect(url_for('routes.signup'))

        return redirect(url_for('routes.login'))
    else:
        return render_template('signup.html')

 
@routes.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    role = request.form.get('roles')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('routes.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)

    if role == 'patient':
        url = 'patientUtility.patient'
    elif role == 'doctor':
        url = 'doctorUtility.doctor'
    elif role == 'insuranceProvider':
        url = 'insuranceProviderUtility.insuranceProvider'  
    else:
        url = 'main.profile'    

    return redirect(url_for(url))   

@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))