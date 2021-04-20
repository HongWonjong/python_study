import re
import requests
import numpy as np
from bs4 import BeautifulSoup
text = '010-1566#7152'

parse = re.sub('[-=.#?:$]', '', text)


# 이제 데이터베이스 파일을 가져와서 원하는 문자열을 제거해보자.

with open("database.txt", "r", encoding = "UTF-8") as f:
    database = f.read()

cleaned_database = re.sub('[<>]', '', database)

cleaned_database = re.sub('["scripts"]', '', cleaned_database)

with open("c_database.txt", "w", encoding = 'UTF-8') as f:
    f.write(cleaned_database)

