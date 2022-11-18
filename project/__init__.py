import imp
from flask import Flask, request,url_for,redirect,session,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_mail import Message
from authlib.integrations.flask_client import OAuth


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    google_oauth = OAuth(app)
    app.config['SECRET_KEY'] = 'root'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:deva@localhost:5432/PatientInsuranceManagement'

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = "carebox28@gmail.com"
    app.config['MAIL_PASSWORD'] = "fbovsoxuziblozxy"
    mail = Mail(app)

    
    @app.route('/resetPassword/')
    def resetPassword():
        return render_template('reset_password.html')

    @app.route('/resetPassword/' , methods=['POST'])
    def resetPassword_post():
        msg = Message()
        msg.subject = "Reset Password - Carebox"
        msg.recipients = ['amitaranade43@gmail.com']
        msg.sender = 'carebox28@gmail.com'
        msg.body = 'Reset password link'
        with app.app_context():
            mail.send(msg)
            return render_template('reset_mail_sent.html')
        


    @app.route('/google/')
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

    @app.route('/authorize')
    def authorize():
            token = google_oauth.google.authorize_access_token()
            return render_template('patient.html')


    
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from project.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from project.models import User
    # blueprint for non-auth parts of app
    from project.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #from project import db, create_app, models
    with app.app_context():
    
        db.create_all()
        db.session.commit()
        

    return app