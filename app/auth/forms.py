
''' Here are classes the define the components of the authentication forms '''


from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import Required, Email, EqualTo
from ..models import User   # User class is imported from the model 

class RegisterForm(Form):
    fname = StringField('First Name', validators=[Required()])
    lname = StringField('Last Name', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message='Passwords do not match')])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    role = SelectField('Select Role', choices=['examiner', 'student'])
    submit = SubmitField('Register')
    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

class LoginForm(Form):
    email = StringField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Login')
    
    