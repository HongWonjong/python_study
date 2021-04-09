import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

episodes = soup.find_all("td", attrs = {"class": "title"})
ratings = soup.find_all("div", attrs = {"class": "rating_type"})
total_rating = 0
numbers = len(list(episodes))
for i in range(numbers):
    print(episodes[i].a.get_text(), ratings[i].strong.get_text())
    total_rating += float(ratings[i].strong.get_text())

print("총 점수", total_rating)
print("평균 점수", total_rating/float(numbers))


#for episode in episodes:
#    print(episode.get_text())
#for episode in episodes:
#    print(episode.a.get_text())
#for episode in episodes:
#    title = episode.a.get_text()
#    link = episode.a["href"]
#    print(title)
#    print("https://comic.naver.com" + link)

