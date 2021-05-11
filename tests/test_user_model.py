import unittest
from app.models import Student, Examiner

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        s = Student(password = 'cat')
        e = Examiner(password = 'cat')
        self.assertTrue(s.password_hash is not None)
        self.assertTrue(e.password_hash is not None)
    
    def test_no_password_getter(self):
        s = Student(password = 'cat')
        e = Examiner(password = 'cat')
        with self.assertRaises(AttributeError):
            s.password
            e.password
    
    def test_password_verification(self):
        s = Student(password = 'cat')
        e = Examiner(password = 'cat')
        self.assertTrue(s.verify_password('cat'))
        self.assertFalse(s.verify_password('dog'))
        
        self.assertTrue(e.verify_password('cat'))
        self.assertFalse(e.verify_password('dog'))
    
    def test_password_salts_are_random(self):
        s = Student(password='cat')
        s2 = Student(password='cat')
        
        e = Examiner(password='cat')
        e2 = Examiner(password='cat')
        
        self.assertTrue(s.password_hash != s2.password_hash)
        self.assertTrue(e.password_hash != e2.password_hash)