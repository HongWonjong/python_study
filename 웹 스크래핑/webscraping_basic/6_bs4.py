import requests
from bs4 import BeautifulSoup
# 이제 네이버 웹툰을 검색해서 링크 정보를 복사해오자.
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#print(soup.title) 
#print(soup.title.get_text())
#print(soup.a)
#print(soup.a.get_text())
#print(soup.a.attrs)
#print(soup.a["href"])
#print(soup.find("a", attrs = {"class": "Nbtn_upload"}))
#print(soup.find(attrs = {"class": "Nbtn_upload"}))
#rank1 = soup.find("li", attrs = {"class": "rank01"})
#print(rank1.a)
#print(rank1.a.get_text())
#print(rank1.next_sibling)
#print(rank1.next_sibling.next_sibling)
#rank2 = rank1.next_sibling.next_sibling
#rank3 = rank2.next_sibling.next_sibling
#print(rank1.get_text())
#print(rank2.get_text())
#print(rank3.get_text())
#print(rank1.parent)
#print(rank1.find_next_sibling("li"))
#print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="사신소년-91화 하지 못한 말")
print(webtoon)