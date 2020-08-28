import requests
import unittest

from unittest.mock import patch

from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import _8Ball
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        return app

class TestViews(TestBase):

    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200) 

    def test_8ballpage_view(self):

        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "A"
                p.return_value.text = "Well, Duh"

            response = self.client.get(url_for('_8ball'))
            self.assertIn(b"A", response.data)
            self.assertIn(b"Well, Duh", response.data)
            self.assertEqual(response.status_code, 200)

        #with patch('requests.get') as g:
        #    with patch('requests.post') as p:
        #    g.return_value = 1
        #    p.return_value = "As I see it, Yes."

        #response = self.client.get(url_for('8ball'))
        #self.assertIn(b1, response.data)
        #self.assertIn(b'As I see it, Yes.', response.data)
        #self.assertEqual(response.status_code, 200)