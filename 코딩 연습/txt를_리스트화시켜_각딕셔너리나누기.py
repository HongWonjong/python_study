import re
import requests
import numpy as np
from bs4 import BeautifulSoup
import json



# 클래스 정의   
class Food:
    def __init__(self, name, recipe, *ingredient):
        self.name = name
        self.recipe = recipe
        self.ingredient = ingredient # 재료는 주재료와 부재료(없어도 만들 수 있는 것)로 나누어 입력

    def sr_2(self, x):                     # 입력한 매개변수의 인덱스에 해당하는 레시피를 출력해주는 함수
        print("음식 이름: ",foods[x].name)
        print("음식 레시피:", foods[x].recipe)
        print("재료:", foods[x].ingredient[0])
        print("양념:", foods[x].ingredient[1])
        

    def sr_1(self, input_name):       # 사용자가 먹고 싶은 음식의 이름을 쳤을 때 해당 인스턴스 객체를 출력해주는 함수
            if foods[i].name == input_name:
                self.sr_2(i)
            

foods = []
dict_recipe = []

# 음식이라는 인스턴스 객체를 만들고, 그 안에 다양한 인스턴스 변수를 넣고 호출할 수 있게 되었다.
#--------------------------------------------

with open("database.txt", "r", encoding = "UTF-8") as f:
    recipes = f.read()

# 읽어 온 텍스트 파일을 리스트화 시켜보자.
recipes = recipes.split(",,")   # 그냥 ,와 구분하기 위한 방침.

#for recipe in recipes:
#   print(type(recipe))  => str     # 이렇게 가져온 리스트의 각 요소는 딕셔너리가 아니라 문자열로 취급되는데 어떻게 할까?


# str로 표현되었지만 실제로는 json 형태이므로, 바꿔주면 된다. import json!

for recipe in recipes:
    d_recipe = json.loads(recipe)      # 디스크에 있는 json 포멧 데이터는 load를, 메모리에 있는 데이터는 loads를 사용한다.
    dict_recipe.append(d_recipe)


print("ddd", dict_recipe)
