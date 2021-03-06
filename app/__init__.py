''' Package constructor for Quizz '''

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
bootstrap = Bootstrap()

csrf = CSRFProtect()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

''' Application factory.
    Takes as argument the name of the current configuration for use,
    creates the the application and initilizes the extensions
'''
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    db.init_app(app)
    bootstrap.init_app(app)
    
    csrf.init_app(app)
    
    login_manager.init_app(app)
    
    # Blueprints registered here
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .ExaminerRoutes import examiners as examiners_blueprint
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(examiners_blueprint, url_prefix='/examiner')
    
    return app