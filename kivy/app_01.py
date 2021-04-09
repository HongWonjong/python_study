import numpy as np
import re  # 정규식 모듈을 호출했다.

a = input("찾고 싶은 레시피를 입력해주세요 >")   # 음식 이름 입력하기
# 클래스 정의   
class Food:
    def __init__(self, name, recipe, *ingredient):
        self.name = name
        self.recipe = recipe
        self.ingredient = ingredient # 재료는 주재료와 부재료(없어도 만들 수 있는 것)로 나누어 입력

    def sr_2(self, x):                     # 입력한 매개변수의 인덱스에 해당하는 레시피를 출력해주는 함수
        print("음식 이름: ",foods[x].name)
        print("음식 레시피:", foods[x].recipe)
        print("주 재료:", foods[x].ingredient[0])
        print("부 재료:", foods[x].ingredient[1])
        

    def sr_1(self, input_name):       # 사용자가 먹고 싶은 음식의 이름을 쳤을 때 해당 인스턴스 객체를 출력해주는 함수
            if foods[i].name == input_name:
                self.sr_2(i)
            

foods = [
    Food("나폴리탄 스파게티", "케찹과 우스터 소스를 기반으로, 소시지, 양파, 버섯등을 볶아서 스파게티를 만든다.", ["파스타면", "케찹", "굴소스"], ["소시지", "양파", "버섯"]),
    Food("간장 계란 볶음밥", "식용유에 밥을 볶은 후 간장으로 간을 맞춰주고, 계란을 풀어서 같이 볶아준다. 마지막으로 참깨나 김 가루 등을 뿌려준다." , ["식용유", "밥", "계란", "간장"], ["참깨", "김 가루"])
]

for i in range(len(foods)):
    foods[i].sr_1(a)

# 음식이라는 인스턴스 객체를 만들고, 그 안에 다양한 인스턴스 변수를 넣고 호출할 수 있게 되었다.
# 이제 필요한 것은
# 1. 음식에 대한 정보를 대량으로 스크래핑 해오는 방법 배우기 => (미완성)
# 2. 사용자가 원하는 음식을 인스턴스 객체 사이에서 찾아서 출력하기 => (완성)
# 3. 사용자가 가지고 있는 ingredient를 기반으로 인스턴스 객체 사이에서 주재료를 만족하는 음식을 찾아서 출력하기, 혹은 거의 만족하는 음식을 찾아서 출력하기 => app_04.py(미완성)
# 4. 이러한 과정들이 일어날 수 있는 앱 인터페이스 제작하기 => app_05.py(미완성)