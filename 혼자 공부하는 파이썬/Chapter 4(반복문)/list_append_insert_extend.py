#리스트에 요소를 추가할 때는 세 가지 방법이 있다. 하나는 append()함수를 사용하는 것.
# 이 함수는 리스트의 뒤에 요소를 추가한다. 1개씩만 추가 가능

list_a = [1,2,3]
print(list_a)

list_a.append(4)

print(list_a)

# 이번엔 insert()함수에 대해 알아보자. 위치를 지정하고 원하는 요소를 넣을 수 있다.
# 당연히 이 경우 기존 해당 위치의 요소부터 하나씩 뒤로 밀리게 된다.
list_a.insert(0, 0)

print(list_a)

# 마지막으로 extend()함수를 사용해보자. 여러개를 한번에 넣을 수 있는데, 대괄호로 
# 묶어주어야 인식한다. 이 함수를 이용해서 리스트와 리스트를 묶을 수도 있다.

list_a.extend([5,6,7])
print(list_a)

list_b = [8,9,10]
list_a.extend(list_b)

print(list_a)