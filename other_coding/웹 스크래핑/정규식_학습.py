import re
import requests
import numpy as np
from bs4 import BeautifulSoup
text = '010-1566#7152'

parse = re.sub('[-=.#?:$]', '', text) # 이렇게 하면 대괄호 안에 해당하는 문자들은 전부 ''으로대체된다.


# 이제 데이터베이스 파일을 가져와서 태그만 지우는 방법을 알아보자. 이 역시 sub 모듈을 사용한다.

#re.sub('regex', '치환문자', 대상문자열)

#with open("database.txt", "r", encoding = "UTF-8") as f:
#    recipes = f.read()
#    recipes = re.sub('(<([^>]+)>)', '', recipes)   # 딕셔너리 내부의 []는 사라지지 않는 것으로 보아 건너뛰는 듯 보인다.
#    print(recipes)

#with open("dict_data.txt", "w", encoding = "UTF-8") as f:
#    f.write(recipes)

