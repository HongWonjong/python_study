# 리스트에서 원하는 값을 가진 요소를 전부 지워보자.

list_test = [1,2,1,2,1,2,1,2]

value = 2

while value in list_test:
    list_test.remove(value)

print(list_test)