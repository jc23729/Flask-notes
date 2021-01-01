#Step 1
#Installing Flask

""""
#we"re gonna run these first 3 lines of code
$ python3 -m venv venv
$ source venv/bin/activate

(venv)$ pip3 install flask

... lots of stuff ...
Successfully installed flask Werkzeug Jinja2 ...
Cleaning up...

"""
##2 Next we want to start a file like app.py

#3 Making An App
# Need to create a “flask application”:

from flask import Flask

app = Flask(__name__)

#Step 4 run Flask
# >use the flask run on command lines

#       Running Flask App
#       (venv) $ flask run
#       (Control-C to quit)

#       If your Flask app file isn’t called app:

#       (venv) $ FLASK_APP=app.py flask run