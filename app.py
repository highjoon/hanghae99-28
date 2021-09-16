from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask_bcrypt import Bcrypt
from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

from setting import MONGODB_HOST, SECRET_KEY


app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config.from_pyfile('setting.py')

client = MongoClient(MONGODB_HOST, 27017)
db = client.dbsparta_28


@app.route('/')
def render_main():
    return render_template("index.html")


@app.route('/login')
def log_in():
    return render_template("logIn.html")


@app.route('/signup')
def sign_up():
    return render_template("signUp.html")


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
            return render_template("logIn.html")

            # message = "이미 등록된 메일 주소입니다."
            # return render_template("logIn.html", message=message)
        if dup_name:
            flash("이미 사용중인 닉네임입니다.")
            return render_template("signUp.html")

        hashed_pw = bcrypt.generate_password_hash(password)
        # bcrypt.check_password_hash(hashed_pw, password).decode('utf-8')

        # hashed_pw = bcrypt.generate_password_hash(password).decode(‘utf - 8’)
        # hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()

        user = {
            "mailId": mailId,
            "password": hashed_pw,
            "nickname": nickName,
            "bootcamp": bootCamp,
            "computerMajor": major,
        }

        users.insert_one(user)
        flash("회원가입이 완료되었습니다. 로그인 창으로 이동합니다.")
        print(user)
        return render_template("logIn.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
