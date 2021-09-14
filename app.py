from flask import Flask, render_template, jsonify, request, session, redirect, url_for
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://13.209.67.42', 27017, username="test", password="test")
db = client.dbsparta_plus_week4
SECRET_KEY = "lambong"
import jwt
import datetime
import hashlib

def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)

@app.route('/api/sign', methods=['GET'])
def api_sign():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    result = db.user.find_one({'id': id_receive, 'pw': pw_hash})

    if result is not None:

        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60 * 2)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
        {
            "typ": "JWT","alg": "HS256"
        }

        return jsonify({'result': 'success', 'token': token})

    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)