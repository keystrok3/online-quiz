from flask import request, redirect, url_for, session
from ..models import Quiz, Questions
from .. import db
from . import main
from flask_login import current_user, login_required

@main.route('/')
def index():
    if current_user.is_authenticated:
        return 'Hey {}'.format(current_user.fname)
    else:
        return 'Hey Stranger, {}'.format(current_user.is_authenticated)
    

# Examiner routes
@main.route('/addnewquiz', methods=['GET', 'POST'])
@login_required
def addnewquiz():
    if request.method == 'POST':
        qname = request.get_json()
        if session.get('role') != 'examiner':
            return 'Unauthorized'
        newquiz = Quiz()
        newquiz.name = qname['name']
        db.session.add(newquiz)
        db.session.commit()
        return 'Successful'
    return 'Problem'

@main.route('/addquestions', methods=['GET', 'POST'])
@login_required
def addquestions():
    if request.method == 'POST':
        qn = request.get_json()
        if session.get('role') != 'examiner':
            return 'Unauthorized'
        qstn = Questions()
        qstn.question_detail = qn['question_detail']
        qstn.option_a = qn['option_a']
        qstn.option_b = qn['option_b']
        qstn.option_c = qn['option_c']
        qstn.option_d = qn['option_d']
        qstn.quiz_id = qn['quiz_id']
        
        db.session.add(qstn)
        db.session.commit()
        return 'Successful'
    return 'Problem'

@main.route('/getqzqns', methods=['GET'])
@login_required
def getqzqns():
    if request.method == 'GET':
        qstnlist = Questions.query.filter_by(quiz_id=1).all()
        return qstnlist[0]
    return 'Problem'
    