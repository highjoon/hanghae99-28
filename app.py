from pymongo import MongoClient
import jwt
import hashlib
from flask_bcrypt import Bcrypt
from flask import Flask, render_template, jsonify, request, redirect, url_for, flash, make_response
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

from setting import MONGODB_HOST, WYC_SECRET_KEY

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config.from_pyfile('setting.py')

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.dbsparta_28
app.secret_key = WYC_SECRET_KEY


# 메인 화면 렌더링 라우터
@app.route('/')
def render_main():
    camps = list(db.detail.find({}, {'_id': False}))
    reviews = list(db.review.find({}, {'_id': False}))
    isLogin = 'false'
    return render_template("index.html", camps=camps, reviews=reviews, isLogin=isLogin)


# 로그인 화면 렌더링 라우터
@app.route('/login')
def render_login():
    return render_template("login.html")


# Review Page
@app.route('/api/review/<keyword>')
def review(keyword):
    camps = list(db.detail.find({'id': keyword}, {'_id': False}))
    reviews = list(db.review.find({'campId': keyword}, {'_id': False}))
    return render_template("review.html", camps=camps, keyword=keyword, reviews=reviews)


# 각 리뷰 항목 DB 저장 및 평점 평균 계산
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

    # DB를 순회하여 campId를 기준으로 일치하는 값을 찾음.
    review_count = list(db.review.find({'campId': campId_receive}, {'_id': False}))
    for count in review_count:
        total = total + float(count['avg'])
        if count['campId'] == campId_receive:
            cnt += 1

    # DB안에 특정 부트캠프의 리뷰가 없다면 avg_count는 처음 받은 평균으로 저장.
    if cnt == 0:
        avg_count = float(avg_receive)
    else:
        # DB안에 특정 부트캠프의 리뷰가 있다면 cnt는 기존의 리뷰 갯수 + 1 (새로 추가된 리뷰)
        cnt += 1
        # DB안에 특정 부트캠프의 리뷰가 있다면 avg_count는 평점 총합 / 리뷰 갯수
        total += float(avg_receive)
        avg_count = total / cnt

    # 전달 받은 값을 review 테이블에 insert.
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


# 평점 평균 계산
@app.route('/api/index/', methods=['GET'])
def get_avg():
    review_count = list(db.review.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'msg': '평점 평균 계산 완료!', 'review_count': review_count})


# 회원가입 페이지 라우터
@app.route('/signup')
def sign_up():
    return render_template("signUp.html")


# 회원가입 시 유효성 검증 및 저장
@app.route('/signup', methods=["GET", "POST"])
def save_userinfo():
    if request.method == "POST":
        mailId = request.form.get("mailId")
        password = request.form.get("pwd")
        nickName = request.form.get("nickName")
        bootCamp = request.form.get("bootCamp")
        major = request.form.get("hasCsMajor")

        if mailId == "" or password == "" or nickName == "" or major == "":
            flash("필수 입력값을 확인해 주십시오.")
            return render_template("signUp.html")

        users = db.users
        dup_mail = users.find_one({"mailId": mailId})
        dup_name = users.find_one({"nickname": nickName})

        if dup_mail:
            flash("이미 등록된 메일 주소입니다.")
            return render_template("login.html")

            # message = "이미 등록된 메일 주소입니다."
            # return render_template("login.html", message=message)
        if dup_name:
            flash("이미 사용중인 닉네임입니다.")
            return render_template("signUp.html")

        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        # hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        user = {
            "mailId": mailId,
            "password": hashed_pw,
            "nickname": nickName,
            "bootcamp": bootCamp,
            "computerMajor": major,
        }

        users.insert_one(user)
        flash("회원가입이 완료되었습니다. 로그인 창으로 이동합니다.")
        return render_login()


# 로그인 시 유효성 검증 및 토큰화
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        mailId = request.form.get("mailId")
        password = request.form.get("pwd")

        if mailId == "":
            flash("메일을 입력해 주세요")
            return render_template("login.html")
        elif password == "":
            flash("패스워드를 입력 하세요")
            return render_template("login.html")

        match_user = db.users.find_one({'mailId': mailId})
        if match_user is not None:
            chk_pw = bcrypt.check_password_hash(match_user['password'], password)
            print('match_user', match_user)
            print('chk_pw', chk_pw)
            if match_user is not None:
                payload = {
                    'email': mailId,
                }
                token = jwt.encode(payload, WYC_SECRET_KEY, algorithm='HS256')
                isLogin = 'true'
                camps = list(db.detail.find({}, {'_id': False}))
                reviews = list(db.review.find({}, {'_id': False}))
                response = make_response(render_template("index.html", camps=camps, reviews=reviews, isLogin=isLogin))
                token = str(token)
                response.set_cookie('token', token)
                print(token)
                return response
        else:
            flash('비밀번호가 일치하지 않습니다.')
            return render_template("login.html")


@app.route('/api', methods=['GET'])
def api():
    # login 요청을 하면서 설정한 쿠키에서 토큰을 받아옴
    token_receive = request.cookies.get('token')
    print('token_receive', token_receive)
    try:
        # 로그인된 jwt 토큰을 디코딩하여 페이로드 확인
        payload = jwt.decode(token_receive, WYC_SECRET_KEY, algorithms=['HS256'])

        # 로그인 정보를 통해 사용자 정보 설정
        user_info = db.users.find_one({"mailId": payload["email"]})
        return render_template('index.html', user_info=user_info)
    # jwt 토큰이 만료되거나 에러 발생시 메인 페이지로 랜더
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("/"))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
