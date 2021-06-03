from flask import request, redirect, url_for, session, render_template, flash
from ..models import Quiz, Questions
from flask_login import current_user, login_required
from  .. import db
from . import examiners
from .forms import NewQuiz, NewQuestion

# Examiners Home - Renders list of quizes
# by current logged in examiner
@examiners.route('/examiner', methods=['GET'])
@login_required
def examiner():
    quizlist = Quiz.query.filter_by(examiner=current_user.id).all()
    return render_template('examiner/quizlist.html', quizlist=quizlist)

# Serve the page with the form for adding quizes
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


# Add new questions, with multiple-choice options and examiner's solution
@examiners.route('/addquestion/<int:id>', methods=['GET', 'POST'])
@login_required
def addquestion(id):
    form = NewQuestion()
    if form.validate_on_submit():
        
        newquestion = Questions()
        newquestion.question_detail = form.question.data
        
        newquestion.option_a = form.option_a.data
        newquestion.option_b = form.option_b.data
        newquestion.option_c = form.option_c.data
        newquestion.option_d = form.option_d.data
        
        newquestion.correct = form.correct.data
        newquestion.quiz_id = id
        
        db.session.add(newquestion)
        db.session.commit()
        
    if form.errors: 
        flash(form.errors)
    return redirect(url_for('examiners.getonequiz', id=newquestion.quiz_id))

# Get all the quizes by the logged in examiner
@examiners.route('/getquizlist', methods=['GET'])
@login_required
def getquizlist():
    quizlist = Quiz.query.filter_by(examiner=current_user.id).all()
    return render_template('examiner/quizlist.html', quizlist=quizlist)


# Get Specific Quiz details, including ability to add, edit, or remove questions
@examiners.route('/getonequiz/<int:id>', methods=['GET'])
@login_required
def getonequiz(id):
    form = NewQuestion()
    quiz = Quiz.query.filter_by(id=id).first()
    quizlist = Quiz.query.filter_by(examiner=current_user.id).all()
    questions = Questions.query.filter_by(quiz_id=quiz.id)
    if quiz == None:
        return redirect(url_for('examiners.examiner'))
    return render_template('examiner/quiz_questions.html', quiz=quiz, questions=questions, quizlist=quizlist, form=form)

# Get one specific question
@examiners.route('/getquestion/<int:id>')
@login_required
def getquestion(id):
    form = NewQuestion()
    try:
        question = Questions.query.filter_by(id=id).first()
        quiz = Quiz.query.filter_by(id=question.quiz_id).first()
        return render_template('examiner/quiz_question.html', quiz=quiz, question=question, form=form)
    except Exception as e:
        print(e)
        return redirect(url_for('examiners.getonequiz', id=question.quiz_id))


    