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