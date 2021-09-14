from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta_28



doc = [
    {'boot_img': 'fast_campus.png',
     'name': '패스트캠퍼스',
     'link': 'https://fastcampus.co.kr/b2b_main?gclid=CjwKCAjw7fuJBhBdEiwA2lLMYVScFE1dw10npuD9xQTCpqoQnpiKTcV2WDNpgFPrUORJuXb3A7XtFRoCZn4QAvD_BwE',
     'tuition': '640만원',
     'period': '6개월',
     'istest': 'X',
     'lang': 'JS,Python',
     'direction': 'Fullstack'
     },

    {'boot_img': 'team_nova.png',
     'name': '팀노바',
     'link': 'https://teamnova.co.kr/index2.php',
     'tuition': '1800만원',
     'period': '12개월',
     'istest': 'X',
     'lang': 'Java,PHP',
     'direction': '통합개발'
     },
    {'boot_img': 'code_squad.png',
     'name': '코드스쿼드',
     'link': 'https://codesquad.kr/',
     'tuition': '396만원',
     'period': '6개월',
     'istest': 'O',
     'lang': 'JS,Swift',
     'direction': 'Web,App 별도운영'
     },

    {'boot_img': 'vanilla_coding.png',
     'name': '바닐라코딩',
     'link': 'https://www.vanillacoding.co/',
     'tuition': '1360만원',
     'period': '4개월',
     'istest': 'O',
     'lang': 'JS',
     'direction': 'Web'
     },

    {'boot_img': 'code_states.png',
     'name': '코드스테이츠',
     'link': 'https://www.codestates.com/course/software-engineering?utm_source=Google_SA&utm_medium=cpc&utm_campaign=SEB&utm_term=%EC%BD%94%EB%93%9C%EC%8A%A4%ED%85%8C%EC%9D%B4%EC%B8%A0&gclid=EAIaIQobChMIiY255-z98gIVWdKzCh0etQc2EAAYASAAEgI8c_D_BwE',
     'tuition': '890만원',
     'period': '4개월~5개월',
     'istest': 'O',
     'lang': 'JS',
     'direction': 'Web'
     },

    {'boot_img': 'we_code.png',
     'name': '위코드',
     'link': 'https://wecode.co.kr/?gclid=EAIaIQobChMIgJT7kO398gIVR6SWCh3gdQzLEAAYASAAEgL8ePD_BwE',
     'tuition': '784만원',
     'period': '3개월',
     'istest': 'X',
     'lang': 'JS,Python',
     'direction': 'Web'
     },
    {'boot_img': 'hanghae99.png',
     'name': '스파르타코딩클럽',
     'link': 'https://hanghae99.spartacodingclub.kr/?utm_source=google_sa&utm_medium=paid&utm_campaign=12074986494&utm_content=116474124916&utm_term=%ED%95%AD%ED%95%B499_525715713510&gclid=EAIaIQobChMI1uWKwu398gIVCXmLCh2HAAUYEAAYASAAEgLKrfD_BwE',
     'tuition': '400만원',
     'period': '3개월',
     'istest': 'O',
     'lang': 'JS,Python',
     'direction': 'Web'
     },

    {'boot_img': '90_factory.png',
     'name': '구공팩토리',
     'link': 'https://90factory.com/',
     'tuition': '650만원(온라인) ~ 850만원(오프라인시 월급 17% 20개월 납부)',
     'period': '3개월',
     'istest': 'X',
     'lang': 'JS,Java,Python',
     'direction': 'Web'
     },
    {'boot_img': 'play_data.png',
     'name': '플레이데이터',
     'link': 'https://playdata.io/',
     'tuition': '822만원(내일배움카드 사용시 무료)',
     'period': '10개월',
     'istest': 'X',
     'lang': 'JS,Python',
     'direction': 'Web'
     }

]

db.review.insert_many(doc)
