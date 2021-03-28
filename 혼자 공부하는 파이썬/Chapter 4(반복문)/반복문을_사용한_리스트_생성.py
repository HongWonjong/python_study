# 파이썬을 제외한 다른 프로그래밍 언어에서는 이런 방식으로 반복문을 이용한 리스트를 생성한다.

# 변수를 선언한다.
array = []

# 반복문을 적용한다.
for i in range(0, 20, 2):
    array.append(i * i)

# 출력합니다.
print(array)