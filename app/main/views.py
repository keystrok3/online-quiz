
''' 
    Defines routes and view functions for the routes for
    the primary functionality of the application.
'''

from flask import request, redirect, url_for, session, render_template
from ..models import Quiz, Questions
from .. import db
from . import main
from flask_login import current_user, login_required       # flask-login is used to manage the user model
from ..auth.forms import RegisterForm
from ..auth.forms import LoginForm

# Renders the registration page if user is not logged in, and user's home page if logged in
@main.route('/', methods=['GET'])
def index():
    form = RegisterForm()
    if current_user.is_authenticated and current_user.role == "examiner":
        return redirect(url_for('examiners.examiner'))
    return render_template('index.html', form=form)

# Renders the log in page
@main.route('/loginpage', methods=['GET'])
def loginpage():
    form = LoginForm()
    return render_template('login.html', form=form)
    