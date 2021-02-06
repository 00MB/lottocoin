from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Name"})
    username = StringField()
    password = PasswordField()
    confirmpassword = PasswordField()
    submit = SubmitField('Register')

class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')