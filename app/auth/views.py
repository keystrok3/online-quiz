from . import auth
from flask import request
from ..models import User
from app.models import db
from flask_login import login_user, logout_user, login_required

# Register new users
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        newuser = request.get_json()
        user = User()
        user.fname = newuser['fname']
        user.lname = newuser['lname']
        user.email = newuser['email']
        user.password = newuser['password']
        user.role = newuser['role']
        db.session.add(user)
        db.session.commit()
        return 'Successful'
    return 'Problem'

# Log In registered users
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        anon = request.get_json()
        user = User.query.filter_by(email=anon['email']).first()
        if user is not None and user.verify_password(anon['password']):
            print(user.email)
            login_user(user)
            return '{} is logged in'.format(user.fname)
        return 'Wrong username  or password'

# Log out active users
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return 'User logged out'