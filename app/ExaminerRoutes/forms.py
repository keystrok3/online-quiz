
""" Classes for forms for examiners functionalities """

from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField, SubmitField, RadioField
from wtforms.validators import Required
from ..models import User   # Import User model from models.py

class NewQuiz(Form):
    name = StringField('Quiz Name', validators=[Required()])
    submit = SubmitField('Create')
    