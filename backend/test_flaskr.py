import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from unicodedata import category

from flaskr import create_app
from models import setup_db, Question, Category
import random


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "tests"
        self.database_path =  "postgresql://{}:{}@{}/{}".format("postgres", "motdepasse", "localhost:5432", self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test1_success(self):
        """Test _____________ """
        res = self.client().get('/categories')

        self.assertEqual(res.status_code, 200)
    def test1_errors1(self):
        """Test _____________ """
        res = self.client().post('/categories')

        self.assertEqual(res.status_code, 405)
    def test1_errors2(self):
        """Test _____________ """
        res = self.client().put('/categories')

        self.assertEqual(res.status_code, 405)
    def test1_errors3(self):
        """Test _____________ """
        res = self.client().delete('/categories')

        self.assertEqual(res.status_code, 405)
    def test1_errors4(self):
        """Test _____________ """
        res = self.client().patch('/categories')

        self.assertEqual(res.status_code, 405)
    
    #test2

 
    def test2_errors1(self):
        """Test _____________ """
        res = self.client().post('/questions')

        self.assertEqual(res.status_code, 200)
    def test2_errors2(self):
        """Test _____________ """
        res = self.client().put('/questions')

        self.assertEqual(res.status_code, 405)
    def test2_errors3(self):
        """Test _____________ """
        res = self.client().delete('/questions')

        self.assertEqual(res.status_code, 405)
    def test2_errors4(self):
        """Test _____________ """
        res = self.client().patch('/questions')

        self.assertEqual(res.status_code, 405)
 

    #test3
    def test3_errors1(self):
        """Test _____________ """
        res = self.client().get('/questions/delete/<id>')

        self.assertEqual(res.status_code, 405)
    def test3_errors2(self):
        """Test _____________ """
        res = self.client().post('/questions/delete/<id>')

        self.assertEqual(res.status_code, 405)
    def test3_errors3(self):
        """Test _____________ """
        res = self.client().patch('/questions/delete/<id>')

        self.assertEqual(res.status_code, 405)
    def test3_errors4(self):
        """Test _____________ """
        res = self.client().put('/questions/delete/<id>')

        self.assertEqual(res.status_code, 405)
  

    #test4

    def test4_success(self):
        """Test _____________ """
        res = self.client().post('/questions/search/')

        self.assertEqual(res.status_code, 200)
    def test4_errors1(self):
        """Test _____________ """
        res = self.client().get('/questions/search/')

        self.assertEqual(res.status_code, 405)
    def test4_errors2(self):
        """Test _____________ """
        res = self.client().put('/questions/search/')

        self.assertEqual(res.status_code, 405)
    def test4_errors3(self):
        """Test _____________ """
        res = self.client().patch('/questions/search/')

        self.assertEqual(res.status_code, 405)
    def test4_errors4(self):
        """Test _____________ """
        res = self.client().delete('/questions/search/')

        self.assertEqual(res.status_code, 405)
  
    #test5

 
    def test5_errors1(self):
        """Test _____________ """
        res = self.client().post('/category/<categori>/questions')

        self.assertEqual(res.status_code, 405)
    def test5_errors2(self):
        """Test _____________ """
        res = self.client().put('/category/<categori>/questions')

        self.assertEqual(res.status_code, 405)
    def test5_errors3(self):
        """Test _____________ """
        res = self.client().patch('/category/<categori>/questions')

        self.assertEqual(res.status_code, 405)
    def test5_errors4(self):
        """Test _____________ """
        res = self.client().delete('/category/<categori>/questions')

        self.assertEqual(res.status_code, 405)
 

    #test6

  
    def test6_errors1(self):
        """Test _____________ """
        res = self.client().get('/play')

        self.assertEqual(res.status_code, 405)
    def test6_errors2(self):
        """Test _____________ """
        res = self.client().put('/play')

        self.assertEqual(res.status_code, 405)
    def test6_errors3(self):
        """Test _____________ """
        res = self.client().patch('/play')

        self.assertEqual(res.status_code, 405)
    def test6_errors4(self):
        """Test _____________ """
        res = self.client().delete('/play')

        self.assertEqual(res.status_code, 405)
    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()