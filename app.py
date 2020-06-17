import os,math
from flask import Flask, render_template, redirect, request, url_for, session, abort, flash, jsonify, json
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from datetime import datetime
import bcrypt
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = 'Sagacity'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

users = mongo.db.users
sagas = mongo.db.sagas
sagaEra = mongo.db.sagaEra
sagaSite = mongo.db.sagaSite


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', sagas=sagas.find())


@app.route('/fetch')
def fetch():
    if request.method == "GET":
        sagaList = []
        for saga in (sagas.find()):
            saga['_id'] = str(saga['_id'])
            sagaList.append(saga)
        return jsonify(sagaList)
        

@app.route('/singleSaga/<saga_id>')
def singleSaga(saga_id):
    theSaga = sagas.find_one({"_id": ObjectId(saga_id)})
    return render_template('singleSaga.html', saga=theSaga)


@app.route('/showSagas/<page>')
def showSagas(page):
    all_sagas = sagas.find().sort([('_id', pymongo.DESCENDING)])
    # count() to count_documents(), see below
    count_sagas = all_sagas.count()
    # goin to have to figure out what offset does actually
    offset = (int(page) - 1) * 2
    limit = 10
    
    sagas_pages = sagas.find().sort(
        [('_id', pymongo.DESCENDING)]).skip(offset).limit(limit)
    # count() to count_documents(), this will replace .find().sort() but it's a mess
    total_pages = int(math.ceil(count_sagas/limit))

    return render_template("showSagas.html",
            sagas_pages=sagas_pages, count_sagas=count_sagas,
            total_pages=total_pages, page=page,)


@app.route('/addSaga')
def addSaga():
    return render_template('addSaga.html', page=1, sagaEra=sagaEra.find(),
     sagaSite=sagaSite.find(), sagas=sagas.find())


@app.route('/insertSaga', methods=['POST'])
def insertSaga():
    completeSaga = {

        'sagaTitle': request.form.get('sagaTitle'),
        'sagaTagline': request.form.get('sagaTagline'),
        'userName': request.form.get('userName'),
        'sagaImage': request.form.get('sagaImage'),
        'Latitude': request.form.get('Latitude'),
        'Longitude': request.form.get('Longitude'),
        'Intro': request.form.get('Intro'),
        'Body': request.form.get('Body'),
        'Conclusion': request.form.get('Conclusion'),
        'eraName': request.form.get('eraName'),
        'siteName': request.form.get('siteName'),
        'dateFull': datetime.today().strftime('%A, %B %d, %Y'),
        'totalLikes': 0
        }

    sagas.insert_one(completeSaga)
    return redirect(url_for('showSagas', page=1))


@app.route('/editSaga/<saga_id>')
def editSaga(saga_id):
    theSaga = sagas.find_one({"_id": ObjectId(saga_id)})
    return render_template('editSaga.html', saga=theSaga)


@app.route('/updateSaga/<saga_id>', methods=["POST"])
def updateSaga(saga_id):
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
        'siteName': request.form.get('siteName')
    })
    return redirect(url_for('showSagas'))


@app.route('/deleteSaga/<saga_id>')
def deleteSaga(saga_id):
    sagas.remove({'_id': ObjectId(saga_id)}),
    return redirect(url_for('showSagas', page=1))


@app.route('/login')
def login():
    if 'username' in session:
        flash('You are logged in as ' + session['username']),
        return render_template('home.html', users=mongo.db.users.find())
    
    return render_template('login.html', users=mongo.db.users.find())


@app.route('/logout')
def logout():
    session.pop('username')
    flash("And you're out...")
    return_url = request.referrer
    return redirect(return_url)


@app.route('/logging', methods=['POST', 'GET'])
def logging():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('home'))

    flash('Invalid username/password combination')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one(
                {'name': request.form['username'],
                 'password': hashpass,
                 'authorName': "",
                 'mySaga': [],
                 'likes': []})
            session['username'] = request.form['username']
            flash("Done, and done")
            return redirect(url_for('home'))
        
        flash('That username already exists!')

    return render_template('register.html', users=mongo.db.users.find())


@app.route('/testSearch', methods=["POST"])
def testSearch():
    if request.method == 'POST':
        search = request.form.to_dict().get('testSearch-name')
        result = []
        print(search)

        collection = mongo.db.stores
        collection.create_index([('name', 'text')])
        answer = collection.find({'$text': {'$search': search}},
        {'$score': {'$meta': "textScore"}})

        for i in answer:
            result.append(i)
        print(result)

        return redirect(url_for('home'))
    
    return redirect(url_for('home'))


@app.route('/liked/<saga_id>', methods=['GET'])
def liked(saga_id):
    
    likes = sagas.find_one({"_id": ObjectId(saga_id)})
    likes = likes["totalLikes"] + 1
    sagas.update_one({'_id': ObjectId(saga_id)}, {
                                "$set": {"totalLikes": likes}})
    # flash("Some message")
    return redirect(request.referrer)


@app.route('/disliked/<saga_id>', methods=['GET'])
def disliked(saga_id):
    
    likes = sagas.find_one({"_id": ObjectId(saga_id)})
    likes = likes["totalLikes"] - 1
    sagas.update({'_id': ObjectId(saga_id)}, {
                                "$set": {"totalLikes": likes}})
    # flash("Some message")
    return redirect(request.referrer)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)