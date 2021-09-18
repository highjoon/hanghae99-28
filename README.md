# 👆 What's your choice?

<!-- ![ScreenShot](./static/image/thumbnail.png) -->

국내에서 운영되고 있는 여러 software Bootcamp 정보를 모아 한 눈에 비교하고, 수강생들의 후기 및 각 Bootcamp별 평점을 확인할 수 있는 웹 어플리케이션 입니다.

<br>

# 👨🏻‍🤝‍👨🏻 팀원

-   윤상준
-   김재용
-   배재경
-   정가람

<br>

# 📅 프로젝트 기간

-   5일 (21.09.13 ~ 21.09.17)

<br>

# ⚙️ 사용 기술 및 환경

## Project Structures

-   flask 서버를 기반으로 jinja2 templete engine 을 이용한 서버사이드렌더링 구조

## 언어

-   python 3
-   MongoDB
-   JavaScript

## 프레임워크 및 라이브러리

-   flask
-   JQuery
-   jinja
-   template engine

<br>

# 🔎 Link

http://projectstudy.shop/

<br>

# 🎥 실행영상

[![실행영상](https://img.youtube.com/vi/sMpx9DWWalk/0.jpg)](https://www.youtube.com/watch?v=sMpx9DWWalk)

<br>

# 🎮 주요 기능

## 1. 로그인, 회원가입

-   회원가입 페이지에서 새로운 회원 정보 등록 요청 시 작성된 사용자 입력값을 받아 서버로 전달 및 db에 저장

-   로그인 요청시 유효한 사용자라면 db에 저장된 사용자 데이터를 통해 입력된 값과 일치하는지 확인 후 회원 인증

-   전달 된 사용자 값 중에서 password를 안전하게 보관할 수 있도록 암호화하는 해싱 알고리즘 (bcrypt)을 통해 새로운 형태로 보관할 수 있다.

-   사용자의 정보는 서버의 시크릿키와 jwt를 통해 인코딩되고 json 형태로 주고받고 싶은 다양한 데이터를 입력하여 주고 받을 수 있으며 유효성을 확인할 수 있다.

## 2. 리뷰 작성, 평점💯 부여 및 등록

-   2-1. 기간, 만족도, 비용, 추천의향 점수 선택 및 코멘트 작성 후 등록

![리뷰 작성 및 점수 기능](./static/image/review_comment.gif)

-   리뷰 작성 및 점수 부여 시

-   2-2. 각 부트캠프 별 리뷰 점수의 평균 확인

![메인페이지 평점평균 출력](./static/image/avg_score.png)
