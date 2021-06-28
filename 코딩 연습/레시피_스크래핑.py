from bs4 import BeautifulSoup
import numpy as np
import requests
import re  # 정규식 모듈을 호출했다.

#-----------레시피 스크래핑-----------------시작----------
url = []     # 왠지는 모르겠는데 한 변수에 289개의 모든 url 주소가 담기지 않아서 반으로 나눠 담았다.
url2 = []

for i in range(1, 145+1):
    url.append("https://www.10000recipe.com/recipe/list.html?cat2=18&order=reco&page={}".format(i))

for i in range(146, 289+1):
    url2.append("https://www.10000recipe.com/recipe/list.html?cat2=18&order=reco&page={}".format(i))

# 초스피드 분야의 모든 페이지를 담았다. 이제 각 페이지마다 보통 40개씩 있는 요리 레시피의 링크로 들어가서 안의 내용을 스크래핑 해오도록 짜면 된다. 
# 스크래핑 된 내용이 바로 Food 클래스에 입력되어서 food 인스턴스가 될 수 있도록 배치를 하자.

database = None        # 모든 레시피에 대한 내용이 문자열 형태로 저장될 변수
for i in range(len(url)):
    res = None
    soup = None
    link_all = None
    link_indiv = None
    http = None
    recipe_total = None
    recipe_name = None
    recipe_ingredient = None
    recipe_step = {} 
    res = requests.get(url[i])
    soup = BeautifulSoup(res.text, "lxml")
    link_all = soup.find_all("a", attrs = {"class": "common_sp_link"})
    print("{}".format(i))
    for i in range(len(link_all)):
        link_indiv = link_all[i]
        http = "https://www.10000recipe.com" + link_indiv["href"]
        res = requests.get(http)
        soup = BeautifulSoup(res.text, "lxml")
        recipe_total = soup.find("script", attrs = {"type" : "application/ld+json"})
        database = recipe_total  
        database = re.sub('(<([^>]+)>)', '', str(database))   # 정규식으로 태그를 제거해버렸지.
        database = database + ",,"   # list화 할 수 있도록!
        with open("database.txt", "a", encoding = 'UTF-8') as f:
            f.write(str(database))
        database = None


    


print("url 변수에 해당하는 모든 레시피가 파일에 저장되었습니다.")
for i in range(len(url2)):
    res = None
    soup = None
    link_all = None
    link_indiv = None
    http = None
    recipe_total = None
    recipe_name = None
    recipe_ingredient = None
    recipe_step = {}
    res = requests.get(url2[i])
    soup = BeautifulSoup(res.text, "lxml")
    link_all = soup.find_all("a", attrs = {"class": "common_sp_link"})
    print("{}".format(i))
    for i in range(len(link_all)):
        link_indiv = link_all[i]
        http = "https://www.10000recipe.com" + link_indiv["href"]
        res = requests.get(http)
        soup = BeautifulSoup(res.text, "lxml")
        recipe_total = soup.find("script", attrs = {"type" : "application/ld+json"})
        database = recipe_total 
        database = re.sub('(<([^>]+)>)', '', str(database))   # 정규식으로 태그를 제거해버렸지.
        database = database + ",,"   # list화 할 수 있도록!
        with open("database.txt", "a", encoding = 'UTF-8') as f:
            f.write(str(database))
        database = None
        
print("url2 변수에 해당하는 모든 레시피가 파일에 저장되었습니다.")

print("모든 레시피에 대한 정보를 저장한 database 파일이 같은 폴더에 생성되었습니다. 프로그램 종료") 

   

#------------레시피 스크래핑------------------끝-----------