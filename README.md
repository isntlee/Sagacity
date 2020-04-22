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