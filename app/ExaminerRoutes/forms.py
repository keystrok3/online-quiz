
""" Classes for forms for examiners functionalities """

from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField, SubmitField, RadioField
from wtforms.validators import Required
from ..models import User   # Import User model from models.py

class NewQuiz(Form):
    name = StringField('Quiz Name', validators=[Required()])
    submit = SubmitField('Create')

class NewQuestion(Form):
    question = StringField('Question', validators=[Required()])
    option_a = StringField('Option A', validators=[Required()])
    option_b = StringField('Option B', validators=[Required()])
    option_c = StringField('Option C', validators=[Required()])
    option_d = StringField('Option D', validators=[Required()])
    correct = StringField('Solution', validators=[Required()])
    submit = SubmitField('Add')