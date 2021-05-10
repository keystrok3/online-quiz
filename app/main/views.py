from flask import request
from ..models import Quiz, Questions
from .. import db
from . import main


@main.route('/addnewquiz', methods=['GET', 'POST'])
def addnewquiz():
    if request.method == 'POST':
        qname = request.get_json()
        print(qname)
        newquiz = Quiz()
        newquiz.name = qname['name']
        db.session.add(newquiz)
        db.session.commit()
        return 'Successful'
    return 'Problem'

@main.route('/addquestions', methods=['GET', 'POST'])
def addquestions():
    if request.method == 'POST':
        qn = request.get_json()
        
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
def getqzqns():
    if request.method == 'GET':
        qstnlist = Questions.query.filter_by(quiz_id=1).all()
        return qstnlist[0]
    return 'Problem'
    