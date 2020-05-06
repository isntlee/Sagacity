import os
from flask import Flask, render_template, redirect, request, url_for, session, abort
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'Sagacity'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    user = mongo.db.user
    login_user = user.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == ['POST']:
        user = mongo.db.user
        existing_user = user.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            user.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')


"""@app.route('/home')
def home():
    return render_template('home.html', sagas=mongo.db.sagas.find())


@app.route('/showSaga')
def showSaga():
    return render_template('showSaga.html', sagas=mongo.db.sagas.find())


@app.route('/addSaga')
def addSaga():
    return render_template('addSaga.html', sagas=mongo.db.sagas.find())


@app.route('/insertSaga', methods=['POST'])
def insertSaga():
    sagas = mongo.db.sagas
    sagas.insert_one(request.form.to_dict())
    return redirect(url_for('showSaga'))


@app.route('/editSaga/<saga_id>')
def editSaga(saga_id):
    theSaga = mongo.db.sagas.find_one({"_id": ObjectId(saga_id)})
    return render_template('editSaga.html', saga=theSaga)


@app.route('/updateSaga/<saga_id>', methods=["POST"])
def updateSaga(saga_id):
    sagas = mongo.db.sagas
    sagas.update({'_id': ObjectId(saga_id)},
    {
        'sagaTitle': request.form.get('sagaTitle'),
        'sagaTagline': request.form.get('sagaTagline'),
        'userName': request.form.get('userName'),
        'sagaImage': request.form.get('sagaImage'),
        'Intro': request.form.get('Intro'),
        'Body': request.form.get('Body'),
        'Conclusion': request.form.get('Conclusion'),
        'eraName': request.form.get('eraName'),
        'locationName': request.form.get('locationName')
    })
    return redirect(url_for('showSaga'))


@app.route('/deleteSaga/<saga_id>')
def deleteSaga(saga_id):
    mongo.db.sagas.remove({'_id': ObjectId(saga_id)}),
    return redirect(url_for('showSaga'))"""


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)