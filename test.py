import os
import unittest
import bcrypt
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from app import app

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
        response = self.mongo.post(
            '/logging',
            data=dict(username='testuser', password='testpass'),
            follow_redirects=True)

        hashpass = bcrypt.hashpw(
                        'testpass'.encode('utf-8'),
                        bcrypt.gensalt()
                       )
        users.insert_one(
                {'name': 'testuser',
                 'password': hashpass,
                 })

        find_user = users.find_one({'name': 'testuser'})

        self.assertIsNotNone(find_user)
        print('User Found. Preparing for Deletion')

        delete_user = users.delete_many({'name': 'testuser'})
        print('User Deleted.')

    def test_deleting_a_saga(self):
        response = self.mongo.post('/deleteSaga/5edfb7ba86bc0fbf85fd8853')
        saga = sagas.find_one({'_id': ObjectId('5edfb7ba86bc0fbf85fd8853')})
        self.assertIsNone(saga)

        print('Recipe Deleted')


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
