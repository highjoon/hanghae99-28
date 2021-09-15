from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta_28

app.config.from_pyfile('config.py')


@app.route('/')
def main():
    camps = list(db.detail.find({}, {'_id': False}))
    return render_template("index.html", camps=camps)


@app.route('/api/review/<keyword>')
def review(keyword):
    camps = list(db.detail.find({'id': keyword}, {'_id': False}))
    return render_template("review.html", camps=camps, keyword=keyword)




# @app.route('/api/review/<keyword>' methods=['GET'])
# def show_review(keyword):
#     reviews = list(db.review.find({'': keyword}, {'_id': False}))
#     return render_template("review.html", keyword=keyword, reviews=reviews)



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
