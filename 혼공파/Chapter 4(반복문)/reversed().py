list_a = [1,2,3,4,5,6,7,8,9]
# 이렇게는 작동이 안 됨
# print(reversed(list_a))

#아래와 같이 써야 함. 그 이유는 204쪽 이터레이터 편에서 알아보자.
print(list(reversed(list_a)))

for i in reversed(list_a):
    print(i)