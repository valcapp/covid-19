import os

message = "Trying to save real runs to database"

os.system("export FLASK_APP=app.py")
# os.system("set FLASK_APP=app.py") # for Windows

if not os.path.exists('migrations'):
    os.system("flask db init")

os.system("flask db migrate -m \"{message}\"")
os.system("flask db upgrade")
