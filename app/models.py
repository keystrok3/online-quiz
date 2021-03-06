from app import create_app, db  # import the application instance the app package constructor as well the db object
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from . import login_manager


''' Quiz, Questions, User, and Attempted Quizzes represent entities in the database '''
class Quiz(db.Model):
    __tablename__ = 'quizes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    questions_list = db.relationship('Questions', backref='questions')
    examiner = db.Column(db.Integer, db.ForeignKey('users.id'))

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question_detail = db.Column(db.String(128))
    option_a = db.Column(db.String(128))
    option_b = db.Column(db.String(128))
    option_c = db.Column(db.String(128))
    option_d = db.Column(db.String(128))
    correct = db.Column(db.Integer)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'))

class User(UserMixin, db.Model):
    __tablename__ = 'users'   
    
    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True) 
    email = db.Column(db.String(64),  unique=True, nullable=False)
    fname = db.Column(db.String(64), nullable=False)
    lname = db.Column(db.String(64), nullable=False)
    role = db.Column(db.String(64), db.CheckConstraint("role == 'student' or role == 'examiner'"))
    password_hash = db.Column(db.String(128))
    
    # Defines a new property for User()
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

# All the students' solutions
class StudentSolution(db.Model):
    __tablename__ = 'studentsolutions'
    id = db.Column(db.Integer, primary_key=True)
    quizname = db.Column(db.Integer, db.ForeignKey('quizes.id'))
    question = db.Column(db.Integer, db.ForeignKey('questions.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    student_solution = db.Column(db.String(64), nullable=False)    
    
# List of students and quizes they've registered for
class StudentQuizList(db.Model):
    __tablename__ = 'studentquizlist'
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'))    

# Students' scores in quizes
class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    score = db.Column(db.Integer)

''' Loads a user from the session '''
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id = user_id).first()

    
    
app = create_app('default')
app.app_context().push()
db.create_all()