# 클래스를 선언합니다.
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

# 학생 리스트를 선언합니다.
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print(students) # 이렇게는 출력이 되지 않는다. self.<식별자>의 형태로 접근해야 인스턴스의 속성을 알 수 있다.

# 인스턴스의 속성에 접근하는 법
print(students[0].name)
print(students[0].korean)
print(students[0].math)
print(students[0].english)
print(students[0].science)
