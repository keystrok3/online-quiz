from app import create_app, db

class Quiz(db.Model):
    __tablename__ = 'quizes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    questions_list = db.relationship('Questions', backref='questions')

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question_detail = db.Column(db.String(128), index=True)
    option_a = db.Column(db.String(128), index=True)
    option_b = db.Column(db.String(128), index=True)
    option_c = db.Column(db.String(128), index=True)
    option_d = db.Column(db.String(128), index=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'))
    
    
app = create_app('default')
app.app_context().push()
db.create_all()