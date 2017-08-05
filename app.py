import os

from flask import Flask, make_response, jsonify, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from flask_restful import Api
from flask_jwt import JWT
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime, timedelta

from db import db

from resources.users import ListUsers


app = Flask(__name__)

CORS(app, supports_credentials=True, resources={r"*": {"origins": "*"}})
app.config['DEBUG'] = True

dbname   = 'mysql+pymysql://root:dinakoiingon@127.0.0.1/geeksolutions'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', dbname)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=1)


app.secret_key = 'wittydev'
db.init_app(app)
api = Api(app)

@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(jsonify(data), code)
    resp.headers.extend(headers or {})
    return resp


api.add_resource(ListUsers, '/users/index')



if __name__ == "__main__":
	app.run()
