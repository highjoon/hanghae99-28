from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta_28
SECRET_KEY = "lambong1"
import jwt
import datetime
import hashlib

@app.route('/')
def main():
    camps = list(db.detail.find({}, {'_id': False}))
    return render_template("index.html", camps=camps)

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
    #except jwt.exceptions.DecodeError:
     #   return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
