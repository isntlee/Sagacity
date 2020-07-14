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
# sagaMap = mongo.db.searchMap
sortBy = ('_id', pymongo.DESCENDING)


@app.route('/')
@app.route('/home')
def home():

    return render_template('home.html', sagas=sagas.find())


# @app.route('/searchMap/<saga_id>', methods=['POST', 'GET'])
# def searchMap(saga_id):
#     searchMapSaga = sagas.find_one({"_id": ObjectId(saga_id)})
#     searchMapCoOrds = {
#         'lat': searchMapSaga['lat'],
#         'lng': searchMapSaga['lng'],
#         }

#     print(searchMapCoOrds)
#     sagaMap.insert_one(searchMapCoOrds)
#     return render_template(
#                             'home.html',
#                             sagas=sagas.find(),
#                             searchMapCoOrds=searchMapCoOrds
#                             )


@app.route('/fetch')
def fetch():
    if request.method == "GET":
        sagaList = []
        for saga in (sagas.find()):
            saga['_id'] = str(saga['_id'])
            sagaList.append(saga)
        return jsonify(sagaList)


# @app.route('/fetchMap')
# def fetchMap():
#     if request.method == "GET":
#         searchMapList = []
#         for coOrds in (sagaMap.find()):
#             coOrds['_id'] = str(coOrds['_id'])
#             searchMapList.append(coOrds)
#         return jsonify(searchMapList)


# -------------------------- Handling Entries ------------------------------- #


@app.route('/singleSaga/<saga_id>')
def singleSaga(saga_id):
    theSaga = sagas.find_one({"_id": ObjectId(saga_id)})
    return render_template('singleSaga.html', saga=theSaga)


# --------------------------------------------------------------------------- #
# -------------------------- Tester Function  ------------------------------- #
# --------------------------------------------------------------------------- #


@app.route('/tester/<page>')
def tester(page):

    limit = 6
    offset = (int(page) - 1) * limit
    all_sagas = sagas.find().sort([('_id', pymongo.DESCENDING)])
    current_saga = (int(page) * limit) - (limit - 1)
    count_sagas = all_sagas.count()
    total_pages = int(math.ceil(count_sagas/limit))

    if int(page) > 1:
        prev_page = int(page) - 1
    else:
        prev_page = page

    if int(page) < total_pages:
        next_page = int(page) + 1
    else:
        next_page = page

    sagas_pages = sagas.find().sort(
        [sortBy]).skip(offset).limit(limit)

    return render_template(
                "tester.html",
                sagas_pages=sagas_pages, current_saga=current_saga,
                count_sagas=count_sagas, total_pages=total_pages,
                page=page, next_page=next_page, prev_page=prev_page)


# --------------------------------------------------------------------------- #
# --------------------------   Tester End ... ------------------------------- #
# --------------------------------------------------------------------------- #


@app.route('/showSagas/<page>')
def showSagas(page):
    all_sagas = sagas.find().sort([('_id', pymongo.DESCENDING)])
    # count() to count_documents(), see below
    count_sagas = all_sagas.count()
    # goin to have to figure out what offset does actually
    limit = 12
    offset = (int(page) - 1) * limit
    sagas_pages = sagas.find().sort(
        [('_id', pymongo.DESCENDING)]).skip(offset).limit(limit)
    total_pages = int(math.ceil(count_sagas/limit))

    return render_template(
                "showSagas.html",
                sagas_pages=sagas_pages, count_sagas=count_sagas,
                total_pages=total_pages, page=page)


@app.route('/mySagas/<page>')
def mySagas(page):
    username = session.get('username')
    my_sagas = sagas.find(
        {'authorName': username}).sort(
            [('_id', pymongo.DESCENDING)]
        )
    count_my_sagas = my_sagas.count()
    limit = 12
    offset = (int(page) - 1) * limit
    # All the changes to be made for showSagas, must be made here
    my_sagas_pages = my_sagas.skip(offset).limit(limit)
    my_total_pages = int(math.ceil(count_my_sagas/limit))

    return render_template(
                "mySagas.html",
                my_sagas_pages=my_sagas_pages, count_my_sagas=count_my_sagas,
                username=username, my_total_pages=my_total_pages, page=page
                )


# ----------------------------------- Add ------------------------------------#


@app.route('/addSaga')
def addSaga():
    return render_template(
                'addSaga.html',
                sagaEra=sagaEra.find(), sagaSite=sagaSite.find(),
                sagas=sagas.find(), page=1
                )


@app.route('/insertSaga', methods=['POST'])
def insertSaga():

    Intro = request.form.get('Intro')
    Body = request.form.get('Body')
    Conclusion = request.form.get('Conclusion')
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
        'Intro': request.form.get('Intro'),
        'Body': request.form.get('Body'),
        'Conclusion': request.form.get('Conclusion'),
        'eraName': request.form.get('eraName'),
        'siteName': request.form.get('siteName'),
        'dateFull': datetime.today().strftime('%A, %B %d, %Y'),
        'dateCard': datetime.today().strftime('%B %d, %Y'),
        'authorName': session['username'],
        # This'll be a future problem, 'username' and 'authorname' confusion
        'wordCount': wordCount,
        'readingTime': readingTime,
        'totalLikes': 0,

        }

    sagas.insert_one(completeSaga)
    return redirect(url_for('showSagas', page=1))


# ------------------------------- Edit/Delete --------------------------------#


@app.route('/editSaga/<saga_id>')
def editSaga(saga_id):
    theSaga = sagas.find_one({"_id": ObjectId(saga_id)})
    return render_template('editSaga.html', saga=theSaga)


@app.route('/updateSaga/<saga_id>', methods=["POST"])
def updateSaga(saga_id):
    sagas.update({'_id': ObjectId(saga_id)}, {

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


# --------------------------- Registration/Login -----------------------------#


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
        if bcrypt.hashpw(
                request.form['pass'].encode('utf-8'),
                login_user['password']
                ) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('home'))

    flash('Invalid username/password combination')


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
            flash("Done, and done")
            return redirect(url_for('home'))
        flash('That username already exists!')

    return render_template('register.html', users=mongo.db.users.find())


# ------------------------------ Search -----------------------------------#


@app.route('/sagaSearch', methods=["POST"])
def sagaSearch():
    if request.method == 'POST':
        search = request.form.to_dict().get('sagaSearch-sagaTitle')
        result = []
        print(search)

        collection = mongo.db.sagas
        collection.create_index([('sagaTitle', 'text')])
        # the index searched is just the titles
        answer = collection.find({'$text': {'$search': search}},
                                 {'$score': {'$meta': "textScore"}}
                                 )

        for i in answer:
            result.append(i)
        # There has to be some way to increase the accuracy of results
        print(result)
        return render_template('sagaSearch.html', searchedSagas=result)

    return redirect(url_for('home'))


# ------------------------------ Likes/Ratings -------------------------------#


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
    dislikes = sagas.find_one({"_id": ObjectId(saga_id)})
    dislikes = dislikes["totalLikes"] - 1
    sagas.update_one({'_id': ObjectId(saga_id)}, {
                                "$set": {"totalLikes": dislikes}})
    # flash("Some message")
    return redirect(request.referrer)


@app.route('/flashed/<saga_id>', methods=['GET'])
def flashed(saga_id):
    flash("Some message")
    return redirect(request.referrer)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)