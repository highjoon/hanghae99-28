from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

app = Flask(__name__)

client = MongoClient('IPadress', 27017, username="아이디", password="비밀번호")
db = client.dbsparta_28

app.config.from_pyfile('config.py')

@app.route('/')
def main():
    return render_template("index.html")


@app.route('/api/review_detail', methods=['GET'])
def show_stars():
    review_detail = list(db.review.find({}, {'_id': False}))
    return jsonify({'review_detail': review_detail})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
