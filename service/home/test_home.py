# coding: utf-8

from flask.ext.testing import TestCase
from service import app


class HomeTestCase(TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def create_app(self):
        return app

    def test_home(self):
        response = self.app.get("/")
        self.assertEquals("ok", response.get_data())
