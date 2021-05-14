from . import auth
from flask import request, session, redirect, url_for, render_template, flash
from ..models import User
from app.models import db
from flask_login import login_user, logout_user, login_required
from .forms import RegisterForm, LoginForm
from .. import main

# Register new users
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            user = User()
            
            user.fname = form.fname.data
            user.lname = form.lname.data
            user.email = form.email.data
            user.password = form.password.data
            user.role = form.role.data
            
            db.session.add(user)
            db.session.commit()
        except:
            flash('An Error Occurred')
            return render_template('index.html', form=form)
        return redirect(url_for('main.loginpage'))

# Log In registered users
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user is not None and user.verify_password(password):
            login_user(user)
            print(user.role)
            if user.role == 'examiner':
                return redirect(url_for('examiners.examiner'))
        else:
            flash('Wrong email or password')
    return redirect(url_for('main.loginpage'))

# Log out active users
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))