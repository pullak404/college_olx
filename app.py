from flask import Flask,render_template,flash
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone


#Create a flask instance
app = Flask(__name__)

#csrf token #hide when uploading to github
app.config['SECRET_KEY'] = "my super secret key"

#add database   
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

#initilize the database
db = SQLAlchemy(app)

#Create a model
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False , unique = True)
    date_added = db.Column(db.DateTime, default=datetime.now(timezone.utc))

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key = True)
    ItemName = db.Column(db.String(100), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    available = db.Column(db.Boolean)
    price = db.Column(db.Integer, nullable = False)
    date_added = db.Column(db.DateTime, default=datetime.now(timezone.utc))


#Create a User Class
class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired()])
    phone = IntegerField("Phone Number",validators=[DataRequired(),Length(min=10,max=10)])
    passwd = PasswordField('New Password', [DataRequired(), EqualTo('confirm', message='Passwords must match')])
    submit = SubmitField("Submit")

class SignUpForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(),Email()])
    phone = IntegerField("Phone Number",validators=[DataRequired(),Length(min=10,max=10)])
    passwd = PasswordField('New Password', [DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    submit = SubmitField("Submit")


#Create a Form Class
class ProductForm(FlaskForm):
    name = StringField("Whats your Name",validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/')
def index():
    return render_template("index.html")

# localhost:5000/user/pullak
@app.route('/product/<ID>')
def product(ID):
    return render_template("product.html",ItemID=ID)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sell')
def sell():
    return render_template('sell.html')


#Custom Error Page

#invalid Url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"),500
