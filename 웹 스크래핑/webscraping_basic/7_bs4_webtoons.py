import requests
from bs4 import BeautifulSoup
# 이제 네이버 웹툰을 검색해서 링크 정보를 복사해오자.
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("a", attrs = {"class":"title"})

for cartoon in cartoons:
    print(cartoon.get_text())