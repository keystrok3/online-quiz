from flask import request, redirect, url_for, session, render_template
from ..models import Quiz, Questions
from .. import db
from . import main
from flask_login import current_user, login_required
from ..auth.forms import RegisterForm
from ..auth.forms import LoginForm

@main.route('/', methods=['GET'])
def index():
    form = RegisterForm()
    return render_template('index.html', form=form)

@main.route('/loginpage', methods=['GET'])
def loginpage():
    form = LoginForm()
    return render_template('login.html', form=form)
    

# Examiner routes
@main.route('/addnewquiz', methods=['GET', 'POST'])
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

@main.route('/addquizquestions', methods=['GET', 'POST'])
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

@main.route('/getquizquestions', methods=['GET'])
@login_required
def getqzqns():
    if request.method == 'GET':
        qstnlist = Questions.query.filter_by(quiz_id=1).all()
        return qstnlist[0]
    return 'Problem'
    