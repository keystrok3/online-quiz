import os
from app import create_app, models
from app.models import Quiz, Questions
from flask_script import Manager, Shell


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, models=models, Quiz=Quiz, Questions=Questions)

manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def test():
    """ Run The unit tests """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()