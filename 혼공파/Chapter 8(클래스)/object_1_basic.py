# 학생 리스트를 선언합니다.

students = [
    {"name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98},
    {"name": "구지연", "korean": 76, "math": 96, "english": 94, "science": 90},
    {"name": "나선주", "korean": 98, "math": 92, "english": 96, "science": 92},
    {"name": "윤아린", "korean": 95, "math": 98, "english": 98, "science": 98},
    {"name": "윤명월", "korean": 64, "math": 88, "english": 92, "science": 92}
    ]

# 학생을 한 명씩 반복하여 출력합니다.

print("이름", "총점", "평균", sep="\t")

for student in students:
    # 점수의 총합과 평균을 구합니다.
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep="\t")

# students도 여러 학생이라는 속성을 가지므로 객체이고, 학생 또한 여러 속성을 가지므로 객체이며, 과목 또한 
# 특정 점수라는 속성을 가질 수 있으므로 객체이다.

# 그런데 이렇게 딕셔너리로 객체를 하나 하나 만들면 조금 복잡하고 귀찮고, 또 딕셔너리를 만드는 과정에서 오타가
# 날 수도 있다. 다름과 같이 딕셔너리를 생성하는 함수로 딕셔너리 생성 코드를 짜 보자.