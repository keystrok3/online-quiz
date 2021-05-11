from app import create_app, db
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from . import login_manager

class Quiz(db.Model):
    __tablename__ = 'quizes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    questions_list = db.relationship('Questions', backref='questions')
    examiner = db.Column(db.Integer, db.ForeignKey('users.id'))

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question_detail = db.Column(db.String(128), index=True)
    option_a = db.Column(db.String(128), index=True)
    option_b = db.Column(db.String(128), index=True)
    option_c = db.Column(db.String(128), index=True)
    option_d = db.Column(db.String(128), index=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'))

class User(db.Model):
    __tablename__ = 'users'   
    
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(64), unique=True, nullable=False)
    fname = db.Column(db.String(64), nullable=False)
    lname = db.Column(db.String(64), nullable=False)
    role = db.Column(db.String(64), db.CheckConstraint("role == 'student' or role == 'examiner'"))
    password_hash = db.Column(db.String(128))
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class AttemptedQuizes(db.Model):
    __tablename__ = 'attemptedquizes'
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    student_score = db.Column(db.Integer)
    

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    
    
app = create_app('default')
app.app_context().push()
db.create_all()