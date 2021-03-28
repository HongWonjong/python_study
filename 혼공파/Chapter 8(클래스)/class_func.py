# 클래스 함수도, 클래스가 가진 기능임을 명시적으로 나타내는 것일 뿐 일반 함수와 큰 차이는 없다.
# 하지만 생성하는 방법이 조금 특이하다. 

class Student: 
    # 클래스 변수
    count = 0
    students = []

    # 클래스 함수
    @classmethod
    def print(cls)