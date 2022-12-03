from project import create_app
from flask_mail import Message
from flask_mail import Mail

app = create_app()
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "carebox28@gmail.com"
app.config['MAIL_PASSWORD'] = "fbovsoxuziblozxy"
mail = Mail(app)


if __name__ == "__main__":
    app.run(debug=True, port=8080)