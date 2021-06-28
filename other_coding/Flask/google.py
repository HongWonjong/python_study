import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from datetime import datetime
import random


client = MongoClient(host="localhost", port=27017)
db = client.myweb
col = db.board

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
for i in range(6):
    url = "https://www.google.com/search?q={}&start={}".format("파이썬", i * 10)
    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.text, "lxml")
    lists = bs.select("#rso")
    for l in lists:
        current_utc_time = round(datetime.utcnow().timestamp() * 1000)
        try:
            title = l.select_one("#rso > div > div > div.tF2Cxc > div.yuRUbf > a > h3").text
            print(title)
            contents = l.select_one("#rso > div > div > div.tF2Cxc > div.IsZvec > div.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc > span").text
            print(contents)
            col.insert_one({
                "name": "테스터",
                "writer_id": "",
                "title": title,
                "contents": contents,
                "view": random.randrange(30, 777),
                "pubdate": current_utc_time
            })
        except Exception:
            print("에러")
            pass
