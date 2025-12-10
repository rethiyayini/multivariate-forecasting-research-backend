import os
import time
import psycopg2
from flask import Flask
from flask_cors import CORS
from .blueprints import login_bp,gold_bp,diesel_bp,tomato_bp,signup_bp  # Correct import path
 # Import the functions
 
app = Flask(__name__)
CORS(app, origins=["http://localhost:3000","http://localhost:3000"])
app.register_blueprint(login_bp)
app.register_blueprint(gold_bp)
app.register_blueprint(diesel_bp)
app.register_blueprint(tomato_bp)
app.register_blueprint(signup_bp)

# def end_headers (self):
#         self.send_header('Access-Control-Allow-Origin', '*')

 
 