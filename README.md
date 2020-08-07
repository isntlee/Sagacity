## Table of Contents
1. [Sagacity] (#sagacity)
2. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
    - [**Wireframes**](#wireframes)

3. [**Features**](#features)
    - [**Current Features**](#current-features)
    - [**Potential Improvements**](#potential-improvements)

4. [**Technologies Used**](#technologies-used)
    - [**Front-End **](#front-ends)
    - [**Back-End **](#back-end)

5. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Unit Testing**](#unit-testing)
    - [**Compatibility**](#compatibility)
    - [**Concerns**](#known-issues)

6. [**Deployment**](#deployment)
    - [**Local**](#local)
    - [**Remote**](#remote)

7. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Coding**](#coding)
    - [**Special Thanks**](#special-thanks)

---

## UX

### User Stories

"** As a user I want to... **" 

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


## Features

### Current Features

**Register Account** 
- Anyone can open/register a personal account. A username/password is required, passwords are hashed to enhance security. 

**Login**
- For users with accounts, the sign-in procedure checks the username/password matches the database record.  

** ** 

** ** 

** ** 

** ** 

** ** 

** ** 

** ** 

** ** 

** ** 


Deployment
-----------------------------------------
Deployment and source control was carried out via GitHub and Heroku. The repository location is as follows:[https://github.com/isntlee/sagacity]

Heroku App Location is as follows [https://sagacity.herokuapp.com/]

Following steps were taken to deploy the website:
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

Sources: 

1. Materialize: https://www.youtube.com/watch?v=gCZ3y6mQpW0&list=PL4cUxeGkcC9gGrbtvASEZSlFEYBnPkmff
2. Flask: https://www.youtube.com/watch?v=bLA6eBGN-_0&feature=emb_title
3. Flash messages in Flask: https://www.youtube.com/watch?v=lcVdZtVvnnk&t=7s
