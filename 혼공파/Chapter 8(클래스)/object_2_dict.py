# 딕셔너리를 리턴하는 함수를 생성합니다.

students = []
def create_student(name, korean, math, english, science):
    dict_student = {"name": name, "korean": korean, "math": math, "english": english, "science": science}
    students.append(dict_student)

create_student("윤인성", 87, 98, 88, 95)
create_student("연하진", 92, 98, 96, 98)
create_student("구지연", 76, 96, 94, 90)
create_student("나선주", 98, 92, 96, 92)
create_student("윤아린", 95, 98, 98, 98)
create_student("윤명월", 64, 88, 92, 92)

print("이름", "총점", "평균", sep = "\t")

for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep = "\t")

# 이전과 같은 실행 결과가 나온다. 
# 현재 총점과 평균을 구하는 처리는 학생을 대상으로만 이루어진다. 따라서 학생을 매개변수로 받는 형태의 함수를
# 만든다면, 코드가 조금 더 균형 잡힐 것이다. 예를 들어서 다음을 직접 코딩해보자.