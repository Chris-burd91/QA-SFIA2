import requests
import unittest
#import requests_mock
#from unittest.mock import patch

from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):

    def create_app(self):

        return app

class TestView(TestBase):

    def test_outcomeview_post(self):
                
        response = self.client.post(url_for('outcome'))
        self.assertEqual(response.status_code ,500)

class TestCase(TestBase):

    def test_outcome_A(self):

        response = self.client.post(url_for('outcome'), json={"key":"A"})
        self.assertIn(b'Well, Duh', response.json)
    
    def test_outcome_B(self):

        response = self.client.post(url_for('outcome'), json={"key":"B"})
        self.assertIn(b"Yes, If you leave me alone..", response.json)

    def test_outcome_C(self):

        response = self.client.post(url_for('outcome'), json={"key":"C"})
        self.assertIn(b"You wish", response.json)

    def test_outcome_D(self):

        response = self.client.post(url_for('outcome'), json={"key":"D"})
        self.assertIn(b"So now you need my help...?", response.json)

    def test_outcome_E(self):

        response = self.client.post(url_for('outcome'), json={"key":"E"})
        self.assertIn(b"You call that a question?...", response.json)

    def test_outcome_F(self):

        response = self.client.post(url_for('outcome'), json={"key":"F"})
        self.assertIn(b"Trump uses me when he decides to go to war", response.json)

    def test_outcome_G(self):

        response = self.client.post(url_for('outcome'), json={"key":"G"})
        self.assertIn(b"Pluto says no and that he's still a Planet", response.json)



        

 
    