import os
from flask import Flask, render_template, redirect, request, url_for, session, abort, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = 'Sagacity'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
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
    return redirect(url_for('showSaga'))


@app.route('/login')
def login():
    if 'username' in session:
        print('You are logged in as ' + session['username']), 
        return render_template('home.html', users=mongo.db.users.find())

    return render_template('login.html', users=mongo.db.users.find())


@app.route('/logging', methods=['POST', 'GET'])
def logging():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('home'))

    return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            print("Done, and done; you're now on file")
            return redirect(url_for('home'))
        
        return 'That username already exists!'

    return render_template('register.html', users=mongo.db.users.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)