import os
import math
import bcrypt
import unittest
from flask import Flask, render_template, redirect, request, url_for, session, flash, jsonify
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from datetime import datetime
from app import app
from os import path
if path.exists("env.py"):
    import env


mongo = PyMongo(app)


users = mongo.db.users
sagas = mongo.db.sagas
sagaEra = mongo.db.sagaEra
sagaSite = mongo.db.sagaSite


class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['DEBUG'] = False
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.mongo = app.test_client()
        app.secret_key = os.environ.get("SECRET_KEY")

    def test_routes(self):

        page = self.mongo.get('/home')
        self.assertEqual(page.status_code, 200)

        page = self.mongo.get('/addSaga')
        self.assertEqual(page.status_code, 200)

        page = self.mongo.get('/login')
        self.assertEqual(page.status_code, 200)

        page = self.mongo.get('/register')
        self.assertEqual(page.status_code, 200)

        page = self.mongo.get('/test')
        self.assertEqual(page.status_code, 404)

        print('All the tests passed')

    def test_successful_registration(self):
        response = self.mongo.post('/logging', data=dict(username='testuser',password='password'), follow_redirects=True)
        print(response)

        find_user = users.find_one({'username': 'testuser'})
        print(find_user)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()