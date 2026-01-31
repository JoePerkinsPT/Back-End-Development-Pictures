from flask import Flask
from . import db

app = Flask(__name__)

# Call the init_db function and store the client
mongodb_client = db.init_db()

# Important: Import routes AFTER the app and client are created
from backend import routes