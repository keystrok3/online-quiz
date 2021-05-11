from . import auth
from flask import request
from ..models import User
from app.models import db


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