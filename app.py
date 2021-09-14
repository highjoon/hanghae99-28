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
    camps = list(db.review.find({}, {'_id': False}))
    return render_template("index.html", camps=camps)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')


@app.route('/review', methods=['GET'])
def review_Detail():
    word_receive = request.args.get('review_give')
    find_one = db.review.find.one({'name': word_receive}, {'id': False})
    boot_img = find_one['boot_img']
    name = find_one['name']
    link = find_one['link']
    tuition = find_one['tuition']
    period = find_one['period']
    istest = find_one['istest']
    lang = find_one['lang']
    direction = find_one['direction']
    return render_template('review.html', boot_img=boot_img, name=name, link=link, tuition=tuition, period=period, istest=istest, lang=lang, direction=direction)


# @app.route('/api/review', methods=['GET'])
# def show_stars():
#     review_detail = list(db.review.find({}, {'_id': False}))
#     return render_template("review.html", review_detail=review_detail)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
