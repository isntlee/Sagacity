# Table of Contents
-[Sagacity](#sagacity)
-[**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
    - [**Wireframes**](#wireframes)
-[**Features**](#features)
    - [**Current Features**](#current-features)
    - [**Potential Improvements**](#potential-improvements)
-[**Technologies**](#technologies)
    - [**Front-End**](#front-end)
    - [**Back-End**](#back-end)
-[**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Unit Testing**](#unit-testing)
    - [**Compatibility**](#compatibility)
    - [**Concerns**](#known-issues)
-[**Deployment**](#deployment)
    - [**Local**](#local)
    - [**Remote**](#remote)
-[**Credits**](#credits)
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
    - jQuery, the classic choice, I decided to make this the corner-stone of my scripts framework.
- [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)
    - Flask is a lightweight WSGI web application framework used to render the back-end with the front.

#### Icons

- [Materialize Icons](https://materializecss.com/icons.html)
    - These are the standard icons that come with Materialize 1.0.0, completely fit for purpose. 
- [Line Awesome 1.3.0](https://icons8.com/line-awesome)
    - An additional series of icons were required, this is a font awesome clone and more than sufficient. 

#### Alerts

 - [Sweet Alerts](https://sweetalert.js.org/docs/)
    - Instead of using the standard alerts-system, I decided to apply this visually improved option. 

### Wireframes

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
- Easily accessible search function, searches through the full collection based on title word choice. 

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


### Potential Improvements 

**Image Storage** 
- Rather than the user inputting a URL, it would be more user-friendly to allow the user to upload an image file from their device. 

**Account Personalisation** 
- To build-in a series of additional options for the user after registering such as saving favourites, hiding personal entries that are still work-in-progress, undo entry deletes and an option to re-set passwords if lost. 

**Geo-location** 
- This would be an additional map feature, that would track the user's location and update the map-centre as the page refreshed. Cost concerns with the API, have delayed its incorporation.

**Error Pages**
- There are two custom error pages for both 404 and 500 errors.

--

## Technologies Used

- [Gitpod](https://www.gitpod.io/) - Used as my IDE for coding.
- [GitHub](https://github.com/) - Used as remote storage of my code.
- [Gimp](https://www.gimp.org/) - Used for editing images.
- [TinyPNG](https://tinypng.com/) - Used to compress images for faster loading.

### Front-End Technologies

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- [jQuery 3.5.0](https://code.jquery.com/jquery/) - Used as the primary JavaScript functionality.
- [Javascript](https://www.javascript.com/) - Used as the primary JavaScript functionality.
- [GoogleMaps API](https://developers.google.com/maps) - Used as the interactive map.
- [Materialize 1.0.0](https://materializecss.com/) - Used as the overall design framework.

### Back-End Technologies

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
- [W3C HTML Validator](https://validator.w3.org) - The Jinja template would only throw errors `{{ variables }}`, `{% for %} {% endfor %}`, etc. Besides this fact, the code is valid. 

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - The code is completely valid, the only warnings concern imported CSS items: the social media buttons, and infowindow details. 

**JavaScript**
- [JShint](https://jshint.com/)
    - The code is valid, all undefined/unused variables are concerned with jQuery, Materialize or SweetAlert
    Three undefined variables:
        - '$' , 'M', 'swal' 

**Python**
- [PEP8 Online](http://pep8online.com/)
    - All python files are all right.

### Automated Testing

- Tests were developed with the Unit testing framework, these tests were applied to the application's routes/forms. See [test.py](https://github.com/isntlee/sagacity/blob/master/test.py) for the full suite of tests. 
- There are two varieties of tests: route/form tests watching clear behaviour and tests verifying actions. 
    - Behavior: testing routes/forms, asserting that all cases behave correctly and returning a request succeed status 200. 
    - Verify actions: the tests created concern writing/deleting from the database; users, sagas, etc, etc. 

### Responsiveness Testing:

Chrome Developer Tools, android/apple mobile phones used to test appearance of site and its various features. 

### User Testing: 




--

## Deployment

### Deployment and source control was carried out via GitHub and Heroku. The repository location is as follows:[https://github.com/isntlee/sagacity]

### Heroku App Location is as follows [https://sagacity.herokuapp.com/]

### Following steps were taken to deploy the website:
1. Database and Tables were created in an Atlas MongoDB account
2. Project workspace was created in GitPod. In this workspace: Flask was installed - `pip3 install flask`.
3. Setup app.py file and imported flask and os - `from flask import Flask. import os`
4. Created an instance of flask - `app = flask(__name__)`
6. Inside the app run() function set the host, ip and debug=true
7. Create a new Heroku App - unique name and EU Server
8. In GitPod login to Heroku through CLI to confirm existance of app. `CLI: heroku login. CLI: heroku apps`.
9. Create a git repository in GitPod. CLI: git init. `CLI: git add . CLI: git commit -m "Initial Commit"`
10. Connect GitPod to Heroku. Use code found on Heroku. `CLI - $heroku git remote -a sagacity`
11. Create requirements.txt file - `CLI: pip3 freeze --local > requirements.txt`
12. Create Procfile - `echo web:python app.py>Procfile`
13. Add and Commit to Git Repository
14. Push to Heroku using code supplied by Heroku
15. `CLI - heroku ps:scale web=1` Command to tell Heroku to run the app
16. Login to Heroku to add config variables including IP, Port, Mongo_DB and Mongo_URI
17. Get Flask to talk to MongoDB - `CLI: pip3 install flask-pymongo` `CLI: pip3 install dnspython`
18. Add extra libraries to app.py - `from flask_pymongo import Pymongo` `from bson.objectid import ObjectID`
19. Add DB connection code to app.py
20. Test connection to DB again to confirm it's working
21. Connect GitHub repository to Heroku using code provided by heroku and github.
22. Set Debug to False

### Sources: 

1. Materialize: https://www.youtube.com/watch?v=gCZ3y6mQpW0&list=PL4cUxeGkcC9gGrbtvASEZSlFEYBnPkmff
2. Flask: https://www.youtube.com/watch?v=bLA6eBGN-_0&feature=emb_title
3. Flash messages in Flask: https://www.youtube.com/watch?v=lcVdZtVvnnk&t=7s
