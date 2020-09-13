from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import os
from config import app_config
#create app method
#run env
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config.from_object(app_config[os.environ.get('FLASK_ENV', 'production')])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# db.init_app(app)
CORS(app)
# cors = CORS(app, support_credentials=True, resources={
#     r"/*": {
#         "origins": "*"
#     }
# })





from app import routes
