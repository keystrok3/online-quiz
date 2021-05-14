
""" Classes for forms for examiners functionalities """

from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField, SubmitField, RadioField
from wtforms.validators import Required
from ..models import User   # User class is imported from the model 

class NewQuiz(Form):
    name = StringField('New Quiz', validators=[Required()])
    submit = SubmitField('Create')