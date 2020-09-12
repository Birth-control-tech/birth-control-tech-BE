from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import os
#create app method
app = Flask(__name__)
cors = CORS(app, support_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import routes




# @app.route("/login")
# @cross_origin(supports_credentials=True)
# def login():
#   return jsonify({'success': 'ok'})
#
# if __name__ == "__main__":
#   app.run(host='0.0.0.0', port=8000, debug=True)
