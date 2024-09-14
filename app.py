from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file


from flask_pymongo import PyMongo


from werkzeug.utils import secure_filename

import urllib.parse

import os


from io import BytesIO

from flask import Flask, render_template, request, redirect, url_for, flash,session,send_file

from flask_pymongo import PyMongo

from pymongo import MongoClient

from bson.objectid import ObjectId

from werkzeug.utils import secure_filename

import os

from io import BytesIO

from flask import Flask, request, jsonify

from pymongo import MongoClient

import base64

import base64



app = Flask(__name__)


app.secret_key = 'your_secret_key'



# MongoDB Atlas connection string


username = urllib.parse.quote_plus('sftghsffth')

password = urllib.parse.quote_plus('giHkXMkhFVwBdfLb')

# Initialize MongoDB collections MongoDB Atlas connection string


app.config["MONGO_URI"] = f"mongodb+srv://{username}:{password}@cluster0.m8r2cjv.mongodb.net/dbname?retryWrites=true&w=majority"

mongo = PyMongo(app)

db = mongo.db

collection = db['techasi']

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/thankyou',methods=["GET", "POST"])
def thank():
    collection.insert_one({'email':request.form.get('email')})
    return render_template('thankyou.html')

