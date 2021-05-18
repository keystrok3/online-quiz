from flask import request, redirect, url_for, session, render_template, flash
from ..models import Quiz, Questions
from flask_login import current_user, login_required
from  .. import db
from . import examiners
from .forms import NewQuiz

# Examiners Home
@examiners.route('/examiner', methods=['GET'])
@login_required
def examiner():
    quizlist = Quiz.query.filter_by(examiner=current_user.id).all()
    return render_template('examiner/quizlist.html', quizlist=quizlist)

@examiners.route('/quizpage', methods=['GET', 'POST'])
@login_required
def quizpage():
    form = NewQuiz()
    return render_template('examiner/newquiz.html', form=form)


# Examiner routes, can only be accessed by logged in user
@examiners.route('/addnewquiz', methods=['GET', 'POST'])
@login_required
def addnewquiz():
    form = NewQuiz()
    if form.validate_on_submit():
        quizname = form.name.data
        
        newquiz = Quiz()
        newquiz.name = quizname
        newquiz.examiner = current_user.id
        db.session.add(newquiz)
        db.session.commit()
        
        return redirect(url_for('examiners.examiner'))
    else:
        flash(form.errors)
    return render_template('examiner/newquiz.html', form=form)

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

# Get all the quizes by the logged in examiner
# @examiners.route('/getquizlist', methods=['GET'])
# @login_required
# def getquizlist():
#     quizlist = Quiz.query.filter_by(examiner=current_user.id).all()
#     return render_template('examiner/quizlist.html', quizlist=quizlist)


# Get Specific Quiz
@examiners.route('/getonequiz/<int:id>', methods=['GET'])
@login_required
def getonequiz(id):
    quiz = Quiz.query.filter_by(id=id).first()
    if quiz == None:
        return redirect(url_for('examiners.examiner'))
    return render_template('examiner/questions.html', quiz=quiz)