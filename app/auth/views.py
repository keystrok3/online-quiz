from . import auth
from flask import request
from ..models import Student, Examiner
from app.models import db


@auth.route('/registerstudent', methods=['GET', 'POST'])
def registerstudent():
    if request.method == 'POST':
        student = request.get_json()
        newstudent = Student()
        newstudent.fname = student['fname']
        newstudent.lname = student['lname']
        db.session.add(newstudent)
        db.session.commit()
        return 'Successful'
    return 'Problem'

@auth.route('/registerexaminer', methods=['GET', 'POST'])
def registerexaminer():
    if request.method == 'POST':
        examiner = request.get_json()
        newexaminer = Examiner()
        newexaminer.fname = examiner['fname']
        newexaminer.lname = examiner['lname']
        db.session.add(newexaminer)
        db.session.commit()
        return 'Successful'
    return 'Problem'