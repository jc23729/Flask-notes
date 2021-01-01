Development Mode
Better to run Flask in “development mode”:

Much better error messages
Automatically re-loads server when code changes on disk
Both of these are very helpful when developing–and very bad for working on a live, production server.

(venv) $ FLASK_ENV=development flask run
Setting Environmental Variables
Can set FLASK_DEV once per terminal session:

>>>can set our virtual enviroment it will automatically will run in >>>development mode every time you run flask run

(venv) $ export FLASK_ENV=development
Add that line to shell config to run on every new terminal session.