import os, math,  unittest
from flask import Flask, render_template, redirect, request, url_for, session, flash, jsonify
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from app import app


app.config['DEBUG'] = False
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


users = mongo.db.users
sagas = mongo.db.sagas
sagaEra = mongo.db.sagaEra
sagaSite = mongo.db.sagaSite


class TestApp(unittest.TestCase):

    def setUp(self):
        self.mongo = app.test_client()

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
        response = self.mongo.post('/logging', data=dict(
            username='testuser', password='password'), follow_redirects=True)
        data = response.data.decode('utf-8')
        find_user = users.find_one({'username': 'testuser'})
        self.assertIsNotNone(find_user)
        print('User Found. Preparing for Deletion')
        delete_user = users.remove({'username': 'testuser'})
        print('User Deleted.')

    def test_deleting_saga(self):
        response = self.mongo.post('/deleteSaga/5ee697e97abe7f5f0513e577')
        saga = sagas.find_one(
            {'_id': ObjectId('5ee697e97abe7f5f0513e577')})
        self.assertIsNone(saga)

        print('Saga Deleted.')

    def tearDown(self):
        sign_out = self.mongo.get('/logout')


if __name__ == '__main__':
    unittest.main()