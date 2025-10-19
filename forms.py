from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired()])
    phone = IntegerField("Phone Number",validators=[DataRequired(),Length(min=10,max=10)])
    passwd = PasswordField('Password', [DataRequired(), EqualTo('confirm', message='Passwords must match')])
    remember = BooleanField('Remember me')
    submit = SubmitField("Login")

class SignUpForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(),Email()])
    phone = IntegerField("Phone Number",validators=[DataRequired(),Length(min=10,max=10)])
    passwd = PasswordField('New Password', validators=[DataRequired()])
    confirm  = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('passwd', message='Passwords must match')])
    submit = SubmitField("Sign Up")
