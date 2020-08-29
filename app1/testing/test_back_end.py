import requests
import unittest

from unittest.mock import patch
import requests_mock

from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import _8Ball
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI='http://127.0.0.1:3306',
               TEST_SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        answer = _8Ball(order="A", answer="Well, Duh")

        db.session.add(answer)
        db.session.commit()
    
    def tearDown(self):

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200) 

    def test_8ballpage_view(self):

        with requests_mock.mock() as g:
            g.get('http://app2:5001/number', json ="A")
            g.get('http://app3:5002/answer', json ={ "A" : "Well, Duh", "B" : "Yes, If you leave me alone..", "C" : "You wish", "D" : "So now you need my help...?", "E" : "You call that a question?...", "F" : "Trump uses me when he decides to go to war", "G" : "Pluto says no and that he's still a Planet", "H" : "Ask me when I care..", "I": "Get a life you Animal!", "I" : "You shouldn't use me to make your life decisions.."})
            g.post('http://app4:5003/generate', json = "Well, Duh")
       

            response = self.client.get(url_for('_8ball'))
            self.assertIn(b"A", response.data)
            self.assertIn(b'{ "A" : "Well, Duh", "B" : "Yes, If you leave me alone..", "C" : "You wish", "D" : "So now you need my help...?", "E" : "You call that a question?...", "F" : "Trump uses me when he decides to go to war", "G" : "Pluto says no and that he\'s still a Planet", "H" : "Ask me when I care..", "I": "Get a life you Animal!", "I" : "You shouldn\'t use me to make your life decisions.."}')
            self.assertIn(b"Well, Duh", response.data)
            self.assertEqual(response.status_code, 200)

        

        #response = self.client.get(url_for('8ball'))
        #self.assertIn(b1, response.data)
        #self.assertIn(b'As I see it, Yes.', response.data)
        #self.assertEqual(response.status_code, 200)