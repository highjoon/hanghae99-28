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


<<<<<<< HEAD


# @app.route('/api/review/<keyword>' methods=['GET'])
# def show_review(keyword):
#     reviews = list(db.review.find({'': keyword}, {'_id': False}))
#     return render_template("review.html", keyword=keyword, reviews=reviews)

=======
@app.route('/api/review/post', methods=['POST'])
def review_post():
    author_receive = request.form['author_give']
    campId_receive = request.form['campId_give']
    overall_receive = request.form['overall_give']
    period_receive = request.form['period_give']
    recommend_receive = request.form['recommend_give']
    tuition_receive = request.form['tuition_give']
    comment_receive = request.form['comment_give']
    avg_receive = request.form['avg_give']

    doc = {
        'author': author_receive,
        'campId': campId_receive,
        'overall': overall_receive,
        'period': period_receive,
        'recommend': recommend_receive,
        'tuition': tuition_receive,
        'comment': comment_receive,
        'avg': avg_receive,
    }

    db.review.insert_one(doc)
    try:
        return jsonify({'result': 'success', 'msg': '리뷰 전송 완료!'})
    except:
        return jsonify({'result': 'success', 'msg': '실패!'})
>>>>>>> 28855a19e89c3f6ce305d150fbd95c3b8dbe7660


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
