from flask import request, redirect, url_for, session, render_template
from ..models import Quiz, Questions
from flask_login import current_user, login_required
from  .. import db
from . import examiners

# Examiners Home
@examiners.route('/examiner', methods=['GET'])
@login_required
def examiner():
    return render_template('examiner/home.html')


# Examiner routes, can only be accessed by logged in user
@examiners.route('/addnewquiz', methods=['GET', 'POST'])
@login_required
def addnewquiz():
    if request.method == 'POST':
        qname = request.get_json()
        if current_user.role != 'examiner':
            return 'Unauthorized'
        newquiz = Quiz()
        newquiz.name = qname['name']
        db.session.add(newquiz)
        db.session.commit()
        return 'Successful'
    return 'Problem'

# examiner route, can only be accessed by logged in user
@examiners.route('/addquizquestions', methods=['GET', 'POST'])
@login_required
def addquestions():
    if request.method == 'POST':
        qn = request.get_json()
        if current_user.role != 'examiner':
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

@examiners.route('/getquizlist', methods=['GET'])
@login_required
def getquizlist():
    if request.method == 'GET':
        quiz = Quiz.query.all()
        if len(quiz) == 0:
            return 'Nothing yet'
        return quiz