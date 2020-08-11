import os
import math
from flask import (
    Flask, render_template, redirect,
    request, url_for, session, flash, jsonify)
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
    # Fetch request, see:
    # https://pythonise.com/series/learning-flask/flask-and-fetch-api,
    # https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
    if request.method == "GET":
        sagaList = []
        for saga in (sagas.find().sort('totalLikes', -1).limit(20)):
            saga['_id'] = str(saga['_id'])
            sagaList.append(saga)
        return jsonify(sagaList)


# --------------------------------------------------------------------------- #
# -------------------------- Handling Entries ------------------------------- #
# --------------------------------------------------------------------------- #


@app.route('/singleSaga/<saga_id>')
def singleSaga(saga_id):
    theSaga = sagas.find_one({"_id": ObjectId(saga_id)})
    return render_template('singleSaga.html', saga=theSaga)


@app.route('/showSagas/<page>', methods=['GET', 'POST'])
def showSagas(page):

    # Pagination, see:
    # https://www.youtube.com/watch?v=PSWf2TjTGNY,
    # https://www.youtube.com/watch?v=Lnt6JqtzM7I

    limit = 6
    offset = (int(page) - 1) * limit
    sagaChoice = ('_id', -1)
    count_sagas = sagas.count_documents({})
    current_saga = (int(page) * limit) - (limit - 1)
    total_pages = int(math.ceil(count_sagas/limit))
    requested = request.form.get("FromHTMLchoice")

    # Sort-By, see:
    # https://stackoverflow.com/questions/10242149/using-sort-with-pymongo,
    # https://stackoverflow.com/questions/8109122/how-to-sort-mongodb-with-pymongo

    if isinstance(requested, str):
        requestChoice = requested.split()
        a = requestChoice[0]
        b = requestChoice[1]
        sagaChoice = (a[2:-2], int(b[:-1]))
    else:
        print("Entries page loading...")

    if int(page) > 1:
        prev_page = int(page) - 1
    else:
        prev_page = page

    if int(page) < total_pages:
        next_page = int(page) + 1
    else:
        next_page = page

    sagas_pages = sagas.find().sort(
                            [sagaChoice]).skip(offset).limit(limit)

    return render_template(
                "showSagas.html", current_saga=current_saga,
                count_sagas=count_sagas, total_pages=total_pages,
                next_page=next_page, prev_page=prev_page, page=page,
                requested=requested, sagas_pages=sagas_pages
                      )


@app.route('/mySagas/<page>', methods=['GET', 'POST'])
def mySagas(page):

    username = session.get('username')
    my_sagas = sagas.find(
        {'authorName': username}).sort(
            [('_id', pymongo.DESCENDING)]
        )
    count_my_sagas = my_sagas.count()

    limit = 6
    offset = (int(page) - 1) * limit
    sagaChoice = ('_id', -1)
    current_saga = (int(page) * limit) - (limit - 1)
    my_total_pages = int(math.ceil(count_my_sagas/limit))
    requested = request.form.get("FromHTMLchoice")

    if isinstance(requested, str):
        requestChoice = requested.split()
        a = requestChoice[0]
        b = requestChoice[1]
        sagaChoice = (a[2:-2], int(b[:-1]))
    else:
        print("Entries page loading...")

    if int(page) > 1:
        prev_page = int(page) - 1
    else:
        prev_page = page

    if int(page) < my_total_pages:
        next_page = int(page) + 1
    else:
        next_page = page

    my_sagas_pages = my_sagas.sort(
                            [sagaChoice]).skip(offset).limit(limit)

    return render_template(
                "mySagas.html", current_saga=current_saga,
                count_my_sagas=count_my_sagas, my_total_pages=my_total_pages,
                next_page=next_page, prev_page=prev_page, page=page,
                requested=requested, my_sagas_pages=my_sagas_pages
                      )


# --------------------------------------------------------------------------- #
# ----------------------------------- Add ------------------------------------#
# --------------------------------------------------------------------------- #


@app.route('/addSaga')
def addSaga():
    return render_template(
                'addSaga.html',
                sagaEra=sagaEra.find(), sagaSite=sagaSite.find(),
                sagas=sagas.find(), page=1
                )


@app.route('/insertSaga', methods=['POST'])
def insertSaga():

    Intro = request.form.get('intro')
    Body = request.form.get('body')
    Conclusion = request.form.get('conclusion')
    words = (Intro + Body + Conclusion).split(" ")
    wordCount = len(words)
    readingTime = math.ceil(wordCount/200)

    completeSaga = {

        'sagaTitle': request.form.get('sagaTitle'),
        'sagaTagline': request.form.get('sagaTagline'),
        'sagaImage': request.form.get('sagaImage'),
        'contextImage': request.form.get('contextImage'),
        'lat': request.form.get('lat'),
        'lng': request.form.get('lng'),
        'intro': request.form.get('intro'),
        'body': request.form.get('body'),
        'conclusion': request.form.get('conclusion'),
        'eraName': request.form.get('eraName'),
        'siteName': request.form.get('siteName'),
        'dateFull': datetime.today().strftime('%A, %B %d, %Y'),
        'dateShort': datetime.today().strftime('%b %d, %Y'),
        'dateCard': datetime.today().strftime('%B %d, %Y'),
        'authorName': session['username'],
        'wordCount': wordCount,
        'readingTime': readingTime,
        'totalLikes': 0,

        }

    sagas.insert_one(completeSaga)
    return redirect(url_for('showSagas', page=1))


# --------------------------------------------------------------------------- #
# ------------------------------- Edit/Delete --------------------------------#
# --------------------------------------------------------------------------- #


@app.route('/editSaga/<saga_id>')
def editSaga(saga_id):
    theSaga = sagas.find_one({"_id": ObjectId(saga_id)})
    return render_template('editSaga.html', saga=theSaga)


@app.route('/updateSaga/<saga_id>', methods=["POST"])
def updateSaga(saga_id):

    Intro = request.form.get('intro')
    Body = request.form.get('body')
    Conclusion = request.form.get('conclusion')
    likes = int(request.form.get('totalLikes'))

    words = (Intro + Body + Conclusion).split(" ")
    wordCount = len(words)
    readingTime = math.ceil(wordCount/200)

    sagas.update({'_id': ObjectId(saga_id)}, {

        'sagaTitle': request.form.get('sagaTitle'),
        'sagaTagline': request.form.get('sagaTagline'),
        'sagaImage': request.form.get('sagaImage'),
        'contextImage': request.form.get('contextImage'),
        'lat': request.form.get('lat'),
        'lng': request.form.get('lng'),
        'intro': request.form.get('intro'),
        'body': request.form.get('body'),
        'conclusion': request.form.get('conclusion'),
        'eraName': request.form.get('eraName'),
        'siteName': request.form.get('siteName'),
        'dateFull': datetime.today().strftime('%A, %B %d, %Y'),
        'dateShort': datetime.today().strftime('%b %d, %Y'),
        'dateCard': datetime.today().strftime('%B %d, %Y'),
        'authorName': session['username'],
        'wordCount': wordCount,
        'readingTime': readingTime,
        'totalLikes': likes,

    })
    return redirect(url_for('showSagas', page=1))


@app.route('/deleteSaga/<saga_id>')
def deleteSaga(saga_id):
    sagas.delete_one({'_id': ObjectId(saga_id)}),
    return redirect(url_for('showSagas', page=1))


# --------------------------------------------------------------------------- #
# --------------------------- Registration/Login -----------------------------#
# --------------------------------------------------------------------------- #


@app.route('/login')
def login():

    # Login/authentication, see:
    # https://pythonspot.com/login-authentication-with-flask/

    if 'username' in session:
        return render_template('home.html', users=mongo.db.users.find())

    return render_template('login.html', users=mongo.db.users.find())


@app.route('/logout')
def logout():
    session.pop('username')

    return redirect(url_for('home'))


@app.route('/logging', methods=['POST', 'GET'])
def logging():

    # Password hashing, see:
    # https://www.youtube.com/watch?v=jJ4awOToB6k

    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(
                request.form['pass'].encode('utf-8'),
                login_user['password']
                ) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('home'))

    flash('Invalid username/password combination')
    return redirect(url_for('login'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(
                        request.form['pass'].encode('utf-8'),
                        bcrypt.gensalt()
                       )
            users.insert_one(
                {'name': request.form['username'],
                 'password': hashpass,
                 })
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        flash('It seems that username is already taken')

    return render_template('register.html', users=mongo.db.users.find())


# --------------------------------------------------------------------------- #
# ------------------------------  Search  ------------------------------------#
# --------------------------------------------------------------------------- #


@app.route('/sagaSearch', methods=["POST"])
def sagaSearch():

    # Text Indexing/Search, see:
    # https://www.youtube.com/watch?v=dTN8cBDEG_Q

    if request.method == 'POST':

        result = []
        search = request.form.to_dict().get('sagaSearch-sagaTitle')
        collection = mongo.db.sagas
        collection.create_index([('sagaTitle', 'text')])
        # the index searched is solely the titles
        answer = collection.find({'$text': {'$search': search}},
                                 {'$score': {'$meta': "textScore"}}
                                 )
        for i in answer:
            result.append(i)

        searchResult = result

        return render_template('sagaSearch.html', searchedSagas=searchResult)

    return redirect(url_for('home'))


# --------------------------------------------------------------------------- #
# ------------------------------ Likes/Ratings -------------------------------#
# --------------------------------------------------------------------------- #


@app.route('/liked/<saga_id>', methods=['GET'])
def liked(saga_id):
    likes = sagas.find_one({"_id": ObjectId(saga_id)})
    likes = likes["totalLikes"] + 1
    sagas.update_one({'_id': ObjectId(saga_id)}, {
                                "$set": {"totalLikes": likes}})

    return redirect(request.referrer)


@app.route('/disliked/<saga_id>', methods=['GET'])
def disliked(saga_id):
    dislikes = sagas.find_one({"_id": ObjectId(saga_id)})
    dislikes = dislikes["totalLikes"] - 1
    sagas.update_one({'_id': ObjectId(saga_id)}, {
                                "$set": {"totalLikes": dislikes}})

    return redirect(request.referrer)


# --------------------------------------------------------------------------- #
# ---------------------------- Errors Handlers -------------------------------#
# --------------------------------------------------------------------------- #


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def somethings_wrong(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
