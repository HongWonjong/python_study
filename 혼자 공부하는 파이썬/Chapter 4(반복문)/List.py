#리스트에 집어넣는 요소는 맨 왼쪽부터 0, 1, 2...의 위치(index)를 부여 받는다. 

list_a = [24, True, False, "개같네", 24]

print(list_a)

print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[3])
# list의 각 인덱스에 새로운 값을 집어넣을 수 있다.
list_a[0] = 2424

print(list_a[0])

# 대괄호의 안에 음수를 넣어 뒤에서부터 요소를 선택할 수 있다.
print(list_a[-2])

# 리스트 접근 연산자를 다음과 같이 이중으로 사용할 수 있다.

print(list_a[3][1])

# 리스트 안에 리스트를 사용할 수도 있다.

list_b = [[1,2,3],[4,5,6],[7,8,9]]
print(list_b)

#리스트에서의 indexError 예시: 존재하지 않는 위치에서 요소를 꺼내려고 할 경우
# IndexError: list index out of range가 뜬다.