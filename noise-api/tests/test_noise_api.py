from application import app
import application.routes
from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app 

class TestView(TestBase):
    def test_get_noise_cat(self):
        response = self.client.post(url_for('noise'), json={"animal":"cat"})
        self.assert200(response)
        self.assertIn(b'meow', response.data)