import requests
import unittest

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
        self.assertEqual(response.status_code ,200)

    #def test_outcome_A(self):

    #    response = self.client.post(url_for('outcome'), json="A")
    #    self.assertIn(b'Well, Duh', response.data)

        

 
    