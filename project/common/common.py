from flask import Blueprint, redirect,render_template,request, url_for
from flask_login import login_required, current_user
from . import db
from .models import Patient, PatientHistory

common = Blueprint('common', __name__)
app = Flask(__name__)
google_oauth = OAuth(app)    

@common.route('/resetPassword/')
def resetPassword():
        return render_template('reset_password.html')

@common.route('/resetPassword/' , methods=['POST'])
def resetPassword_post():
    msg = Message()
    msg.subject = "Reset Password - Carebox"
    msg.recipients = ['amitaranade43@gmail.com']
    msg.sender = 'carebox28@gmail.com'
    msg.body = 'Reset password link'
    with app.app_context():
        mail.send(msg)
        return render_template('reset_mail_sent.html')
        
@common.route('/google/')
def google(): 
        CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
        google_oauth.register(
        name='google',
                client_id='1091902576282-ckdfagtps3648hmrm2u2tgnv2fhrvial.apps.googleusercontent.com',
                client_secret='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',
                server_metadata_url=CONF_URL,
                client_kwargs={
                    'scope': 'openid email profile'
                }
        )
        redirect_uri = url_for('authorize', _external=True)
        print(redirect_uri)
        return google_oauth.google.authorize_redirect(redirect_uri)

@common.route('/authorize')
def authorize():
        token = google_oauth.google.authorize_access_token()
        return render_template('patient.html')

