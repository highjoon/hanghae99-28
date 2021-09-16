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
SECRET_KEY = "lambong1"

app.config.from_pyfile('config.py')


# Main Page
@app.route('/')
def main():
    camps = list(db.detail.find({}, {'_id': False}))
    reviews = list(db.review.find({}, {'_id': False}))
    return render_template("index.html", camps=camps, reviews=reviews)


# Review Page
@app.route('/api/review/<keyword>')
def review(keyword):
    camps = list(db.detail.find({'id': keyword}, {'_id': False}))
    reviews = list(db.review.find({'campId': keyword}, {'_id': False}))
    return render_template("review.html", camps=camps, keyword=keyword, reviews=reviews)


@app.route('/api/review/', methods=['POST'])
def review_post():
    author_receive = request.form['author_give']
    campId_receive = request.form['campId_give']
    overall_receive = request.form['overall_give']
    period_receive = request.form['period_give']
    recommend_receive = request.form['recommend_give']
    tuition_receive = request.form['tuition_give']
    comment_receive = request.form['comment_give']
    avg_receive = request.form['avg_give']

    # DB안에 저장되어있는 특정 부트캠프의 평점 총합.
    total = 0
    # DB안에 저장되어있는 특정 부트캠프의 리뷰 갯수.
    cnt = 0

    review_count = list(db.review.find({'campId': campId_receive}, {'_id': False}))
    for count in review_count:
        total = total + float(count['avg'])
        if count['campId'] == campId_receive:
            cnt += 1

    # DB안에 특정 부트캠프의 리뷰가 없다면 avg_count는 처음 받은 평균으로 저장.
    if cnt == 0:
        avg_count = float(avg_receive)
    else:
        # DB안에 특정 부트캠프의 리뷰가 있다면 avg_count는 평점 총합 / 리뷰 갯수
        cnt += 1
        total += float(avg_receive)
        avg_count = total / cnt

    print(avg_count)

    # 평균 구해지면 return 값으로 평균을 html로 전달.
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


# Login Page

@app.route('/api/sign_in', methods=['GET'])  # 실제 DB에 대조하는 곳
def api_sign_in():
    id_receive = request.form['id_give']  # ID 기존으로 받아줌
    pw_receive = request.form['pw_give']  # PW 해시처리해서 암호화해서 받아줌

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()  # hash값 생성
    result = db.user.find_one({'id': id_receive, 'pw': pw_hash})  # 매칭 안되면

    if result is not None:
        payload = {
            'id': id_receive,  # login.html 에서 로그인 성공해서 토큰값 발행되면 실행되서 결과값 나오는곳
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60 * 2)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
        {"typ": "JWT", "alg": "HS256"}

        return jsonify({'result': 'success', 'token': token})

    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


@app.route('/api/nick', methods=['GET'])
def api_valid():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        print(payload)

        userinfo = db.user.find_one({'id': payload['id']}, {'_id': 0})
        return jsonify({'result': 'success', 'nickname': userinfo['nick']})
    except jwt.ExpiredSignatureError:

        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    # except jwt.exceptions.DecodeError:
    #   return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)