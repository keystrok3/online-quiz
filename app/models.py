from app import create_app, db

class Quiz(db.Model):
    __tablename__ = 'quizes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    questions_list = db.relationship('Questions', backref='questions')
    examiner = db.Column(db.Integer, db.ForeignKey('examiners.id'))

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question_detail = db.Column(db.String(128), index=True)
    option_a = db.Column(db.String(128), index=True)
    option_b = db.Column(db.String(128), index=True)
    option_c = db.Column(db.String(128), index=True)
    option_d = db.Column(db.String(128), index=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'))

class Examiner(db.Model):
    __tablename__ = 'examiners'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(64), index=True)
    lname = db.Column(db.String(64), index=True)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True) 
    fname = db.Column(db.String(64), index=True)
    lname = db.Column(db.String(64), index=True)

class AttemptedQuizes(db.Model):
    __tablename__ = 'attemptedquizes'
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    student_score = db.Column(db.Integer)
    
    
    
app = create_app('default')
app.app_context().push()
db.create_all()