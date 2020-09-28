[**sagacity**](https://sagacity.herokuapp.com/)

# **sagacity**

This site was created to fill a niche, because for all of Dublin's local history collections none are particularly interactive or user-friendly. The central ambition of the project was to make this site as inclusive as possible, that actively encourages participation as the project is a public collection of local stories. And as the project was being submitted that process had definitely begun with several entries from several separate local sources. 

---

- [**Table of Contents:**](#table-of-contents)
    - [**UX**](#ux)
        - [**User Stories**](#user-stories)
        - [**Design**](#design)
        - [**Wireframes**](#wireframes)
    - [**Features**](#features)
        - [**Current Features**](#current-features)
        - [**Potential Improvements**](#potential-improvements)
    - [**Technologies**](#technologies)
        - [**Front-End**](#front-end)
        - [**Back-End**](#back-end)
    - [**Testing**](#testing)
        - [**Validators**](#validators)
        - [**Automated Testing**](#automated-testing)
        - [**Compatibility**](#compatibility)
        - [**User Testing**](#user-testing)
    - [**Deployment**](#deployment)
        - [**Local**](#local)
        - [**Remote**](#remote)
    - [**Credits**](#credits)
        - [**Coding**](#coding)
        - [**Content**](#content)
        - [**Special Thanks**](#special-thanks)

---

## UX

### User Stories

"**As a user I want to...**" 

- be informed of the site's purpose and functions.
- navigate easily through the entries.
- navigate the map, and view various entries.  
- browse the site as a guest.
- create a user profile, log in and out.
- add, edit and delete my own entries through my user account.
- like/dislike a saga, as long as I am logged in as a user.
- receive an error message if I am unable to login or register.
- be able to access the site from any device (mobile, tablet, desktop).
- search easily for a entry.
- see the total likes/dislikes of an entry.
- share an entry on an variety of platforms. 
- be able to see the total number of entries.
- be able to see the details of the entry.
- be prompted to sign up or add an entry.

### Design

#### Framework

- [Materialize 1.0.0](https://materializecss.com/)
    - Materialize is a framework, created and designed by Google, that emphasizes a modern and clean layout. 
- [jQuery 3.5.0](https://jquery.com/y/)
    - jQuery, the classic choice, I decided to make this a crucial part of my scripts framework.
- [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)
    - Flask is a lightweight WSGI web application framework used to render the back-end with the front.

#### Aesthetic

The core ambition of the site is to make the material/sagas as interesting as possible. The aesthetic was chosen to make the text/pictures of the entries take centre stage. This is achieved by bold uncluttered text, and a warm contrast of two key colours.

- (#FAFAFA) (**off-white** - *central color*)
- (#FF9F00)(**off-orange, slightly** - *contrast color*)

#### Icons

- [Materialize Icons](https://materializecss.com/icons.html)
    - These are the standard icons that come with Materialize 1.0.0, completely fit for purpose. 
- [Line Awesome 1.3.0](https://icons8.com/line-awesome)
    - An additional series of icons were required, this is a font awesome clone and more than sufficient. 

#### Alerts

 - [Sweet Alerts](https://sweetalert.js.org/docs/)
    - Instead of using the standard alerts-system, I decided to apply this visually improved option. 

### Wireframes

- The wireframes for this site were made with [draw.io](https://www.draw.io/), and accessible in the folder [wireframes](https://github.com/isntlee/sagacity/tree/master/wireframes)

-- 

## Features

### Current Features

**Register** 
- Anyone can open/register a personal account. A username/password is required, passwords are hashed to enhance security. 

**Login/Logout**
- For users with accounts, the sign-in procedure checks that the username/password matches the database record.  

**View Entries** 
- This is the *Show Sagas* page or the *My Sagas* page, all entries are listed by date added, this criteria changed by selecting sort-by options.   

**Search** 
- Easily accessible search function, searches through the full collection based on title word-choice. 

**Add Entry** 
- Create or add a new entry/saga. There are several required conditions to meet to add an entry such as title, tagline, image, etc, etc. 

**View Entry**
- Read saga/entries in full, from the *Show Sagas* page, *My Sagas* page or from the map marker's "Full page reader" option. There are further options on the view page: 
    - Like/dislike the entry, it's only on this view page that both buttons are active if the user is logged-in. 
    - Find on map, this button returns the user to the map. 
    - Social media buttons, availible for the user to share this entry on a range of platforms.     

**Update Entry** 
- Update or edit your saga/entry, as the option is only availiable with user's own entries.  

**Delete Entry** 
- Delete your saga/entry, as the option is only availiable with user's own entries. 

**Map**
- This is another means of displaying entries, the user is encouraged to provide co-ordinates with their entry as then the entry/saga will be discoverable on the map. However, only the twenty most liked entries/sagas are discoverable on the map as loading periods are a concern.

**Map Reader**
- On the map, if the user selects a marker the full entry is there availible to read within a mini-reader. The user is informed of the entry length and the option of the full-page reader. 

**Pagination**
- Navigation method that organizes the entries into pages, the number of pages depends on the amount of entries displayed per page.

**Sort-By**
- Navigation method that organizes entries by set criteria whether the date added or the number of likes/dislikes added by various users. 

**Error Pages**
- There are two custom error pages for both 404 and 500 errors.



### Potential Improvements 

**Image Storage** 
- Rather than the user inputting a URL, it would be more user-friendly to allow the user to upload an image file from their device. 

**Account Personalisation** 
- To build-in a series of additional options for the user after registering such as saving favourites, hiding personal entries that are still work-in-progress, undo entry deletes and an option to re-set passwords if lost. 

**Geo-location** 
- This would be an additional map feature, that would track the user's location and update the map-centre as the page refreshed. Potential cost concerns with the API have delayed its incorporation.

**Like/dislike buttons**
- The current format only restricts the user to voting once per refresh, with this vote altering the 'likes' DB record. With additional time, there would have been a framework in place to track whether a user had voted for an entry or not, limiting that user to only ever adding one upvote or one downvote. 

--

## Technologies

- [Gitpod](https://www.gitpod.io/) - Used as my IDE for coding.
- [GitHub](https://github.com/) - Used as remote storage of my code.
- [GIMP](https://www.gimp.org/) - Used for editing images.
- [TinyPNG](https://tinypng.com/) - Used to compress images for faster loading.

### Front-End

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- [Javascript](https://www.javascript.com/) - Used as primary JavaScript functionality.
- [jQuery 3.5.0](https://code.jquery.com/jquery/) - Used as secondary JavaScript functionality.
- [GoogleMaps API](https://developers.google.com/maps) - Used as the interactive map.
- [Materialize 1.0.0](https://materializecss.com/) - Used as the overall design framework.

### Back-End

- **Flask**
    - [Flask 1.1.2](http://flask.pocoo.org/) - Used as the microframework.
    - [Jinja 2.11](http://jinja.pocoo.org/docs/2.10/) - Used for templating with Flask.
    - [Bcrypt 3.1.7](https://www.npmjs.com/package/bcrypt) - Bcrypt is a password-hashing function.
- **Heroku**
    - [Heroku](https://www.heroku.com) - Used for the app hosting.
- **Python**    
    - [Python 3.8.5](https://www.python.org/) - Used as for back-end programming.
    - [MongoDB Atlas](https://www.mongodb.com/) - Used to store my database onilne.
    - [PyMongo 3.10.1](https://api.mongodb.com/python/current/) - Used as the Python API for MongoDB.

--

## Testing 

### Validators

**HTML**
- [W3C HTML Validator](https://validator.w3.org) - The Jinja template solely throw errors `{{ variables }}`, `{% for %} {% endfor %}`, etc. Besides this fact, the code is valid. However, in one file "base.html" errors are thrown over the use of <br>, these have been retained due to time constraints. 

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - The code is completely valid, the only warnings concern imported CSS items: the social media buttons, and infowindow details. 

**JavaScript**
- [JShint](https://jshint.com/)
    - The code is valid, all undefined/unused variables are concerned with jQuery, Materialize and SweetAlert
    - The three undefined variables:
        '$' , 'M', 'swal' 
- [JSLint](https://jslint.com/)
    - For JS file, there are two warnings concerning unexpected use of terms with the search-bar code. These unexpected terms are both "for" as in those used in a "for" loop, this is not a serious concern.  
    - For jQuery, all the warning are particularly minor and centre around undeclared/unexpected terms, the major warnings are about "$" or "document". This is not that helpful.   

**Python**
- [PEP8 Online](http://pep8online.com/)
    - All python files are all right.

### Automated Testing

- Tests were developed with the Unit testing framework, these tests were applied to the application's routes/forms. See [test.py](https://github.com/isntlee/sagacity/blob/master/test.py) for the full suite of tests. Unit-tests are run from CLI with the command: "python3 test.py"
- There are two varieties of tests: route/form tests watching clear behaviour and tests verifying actions. 
    - Behavior: testing routes/forms, asserting that all cases behave correctly and returning a request succeed status 200. 
    - Verify actions: the tests created concern writing/deleting from the database; users, sagas, etc, etc. 

### Compatibility

**Mobile**
- Chrome Developer Tools, Android(Samsung A5/Galaxy S8) and Apple(Iphone 8) mobile phones used to test appearance of site and its various features. There are very minor differences between android/ios but all are cosmetic e.g. fonts displaying slightly differently, pages scrolling more fluidly or the map being more immediately responsive on ios. 

**Desktop**
- Google Chrome, Microsoft Edge, Mozilla Firefox all work and display correctly, testing done on a local system. Testing of Safari has only been conducted on [BrowserStack](https://www.browserstack.com/), the site works correctly. 


### User Testing: 

Manual tests were carried out and the testing process was as follows:

**Landing Page**
 - Click "sagacity" and verify that home page appears.
 - Click on Sagas button  - verify redirect to view entries/sagas page.
 - If user is not logged in “Login” should be displayed in the navigation bar and clicking this link will bring you to the login page.
 - Search Button - click to open search bar.
 - Map Button - click and verify if redirected to map where twenty markers should load. 

**User Account**

###### Register Page
- Verify that clicking on the link brings user to the registration page. 
- Both fields required for registration. 
- Tested registering successfully and was returned to the homepage.
- Verify that username must be unique - message appears if details are not unique.

###### Login Page
- Verified that the login link directs to the login page
- If user enters an incorrect set of details, the error message will fire. 
- If user enters the correct login details they are returned to the homepage. 

###### Add Sagas
- User can only add an entry/saga if they are logged in.
- Verified that only particular fields are required.
- Confirmed that entry is added to the database and by marking it on site.

###### Edit Sagas
- User can only add an entry/saga if they are logged in.
- On the singleSaga page, verified that the edit button is only displayed if logged in.
- Verified that only particular fields are required, but that all filled categories appear in-full on form. 
- Confirmed that entry is added to the database and by marking it on site.

###### Delete Sagas
- On the singleSaga page, verified that the delete button is only displayed if logged in.
- Confirmed that the saga is deleted by checking database.

###### My Sagas
- Verified that only sagas added by the user are displayed.
- Confirm that the user only sees this page if logged in.
- Pagination is present only if user has more than 6 entries selected.

###### Logout
- Verified that the user is returned to home and logged out.

**singleSaga Page**
- Confirm that clicking on the "Read More" Sagas link directs to a detailed version of the entry/saga.
- Verified that the correct details are in the correct positions for each entry.
- Verified the social media links are working properly.
- Confirmed that the user like/dislike buttons are working correctly, and that user must be logged in to vote.

**Search by Keyword**
- Enter a terms into the search form and confirm that the correct results are returned with paginaition if neccessary.

**Error Pages**
 - Try going to [http://sagacity.herokuapp.com/404](http://sagacity.herokuapp.com/404) and see a custom 404 error.
 - Confirmed that there was a working link back to safety.

--

## Deployment

#### Source control and deployment was carried out primarilly via [GitHub](https://github.com/isntlee/sagacity) and [Heroku](https://sagacity.herokuapp.com/)

### Local Deployment

Please note - in order to run this project locally on your own system, you will need the following installed:
- [Python3](https://www.python.org/) to run the application.
- [PIP](https://pip.pypa.io/en/stable/) to install app requirements.
- [Gitpod](https://www.gitpod.io/) as IDE.
- [GIT](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for version control.
- [MongoDB](https://www.mongodb.com) to develop your own database.

1. Database created in an Atlas MongoDB account
2. Project workspace was created in GitPod. In this workspace: Flask was installed - `pip3 install flask`.
3. Setup app.py file and imported flask and os - `from flask import Flask. import os`
4. Created an instance of flask - `app = flask(__name__)`
5. Inside the app run() function set the host, ip and debug=true
6. Create a `.env` file with your credentials. 
7. Create a git repository in GitPod. CLI: git init. `CLI: git add . CLI: git commit -m "Initial Commit"`
8. Get Flask to talk to MongoDB - `CLI: pip3 install flask-pymongo` `CLI: pip3 install dnspython`
9. Add extra libraries to app.py - `from flask_pymongo import Pymongo` `from bson.objectid import ObjectID`
10. Add DB connection code to app.py
11. Test connection to DB again to confirm it's working
12. Set Debug to False


### Remote Deployment

This site is currently deployed here on [**Heroku**](https://sagacity.herokuapp.com/) using the **master** branch on GitHub. To implement this project on Heroku, the following steps were taken:

1. Create a new Heroku App - unique name
2. In GitPod login to Heroku through CLI to confirm existance of app. `CLI: heroku login. CLI: heroku apps`.
3. Connect GitPod to Heroku. Use code found on Heroku. `CLI - $heroku git remote -a sagacity`
4. Create requirements.txt file - `CLI: pip3 freeze --local > requirements.txt`
5. Create Procfile - `echo web:python app.py>Procfile`
6. Add and Commit to Git Repository
7. Push to Heroku using code supplied by Heroku
8. `CLI - heroku ps:scale web=1` Command to tell Heroku to run the app
9. Login to Heroku to add config variables:
    - **IP**: 0.0.0.0
    - **Port**: 8080
    - **SECRET_KEY**: your secret key
    - **Mongo_URI**: link to Mongo DB


### Database setup/collections:

**sagaEra**
```
_id: <ObjectId>
eraName: <string>
```

**sagaSite**
```
_id: <ObjectId>
siteName: <string>
```

**users**
```
_id: <ObjectId>
name: <string>
password: <string>
```

**sagas**
```
_id: <ObjectId>
sagaTitle: <string>
sagaTagline: <string>
sagaImage: <string>
lat: <string>
lng: <string>
intro: <string>
body: <string>
conclusion: <string>
eraName: <string>
siteName: <string>
total_time: <string>
dateFull: <string>
dateCard: <string>
authorName: <string>
wordCount: <int 32>
readingTime: <int 32>
totalLikes: <int32>
```

## Credits: 

### Coding

- [Materialize](https://www.youtube.com/watch?v=gCZ3y6mQpW0&list=PL4cUxeGkcC9gGrbtvASEZSlFEYBnPkmff)
- [GoogleMaps JSON objects](https://www.youtube.com/watch?v=mfjqLmD6Li8)
- [GoogleMaps API](https://www.youtube.com/watch?v=pFpBibg6nac)
- [Pagination Flask/MongoDB](https://www.youtube.com/watch?v=Lnt6JqtzM7I)
- [Pagination Flask/MYSQL](https://www.youtube.com/watch?v=PSWf2TjTGNY)
- [Unit-testing](https://www.youtube.com/watch?v=6tNS--WetLI)
- [Text Indexing](https://www.youtube.com/watch?v=dTN8cBDEG_Q)
- [Password Hashing](https://www.youtube.com/watch?v=jJ4awOToB6k)
- [Flask](https://www.youtube.com/watch?v=bLA6eBGN-_0)
- [Flash messages](https://www.youtube.com/watch?v=lcVdZtVvnnk)

### Content 

- [Google Images](https://images.google.com/) 
    - All images taken from Google Image searches. 
- [Favicon.io](https://favicon.io/) 
    - Designed and produced flavicon 

### Special Thanks

- [Precious Ijege](https://github.com/precious-ijege) 
    - My Code Institute mentor
- [Corey Schafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) 
    - His tutorials have been essential research for many.
