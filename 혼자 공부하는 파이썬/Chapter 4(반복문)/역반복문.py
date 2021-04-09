# 역반복문을 만드는 첫 번째 방법은 range의 매개변수를 세 개 사용하는 방법이다.
for i in range(4, 0-1, -1):
    print("현재 반복 변수: {}".format(i))

# 2번째 방법은 reversed()함수를 사용하는 방법이다.
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))

# reversed()함수는 리스트 등에도 적용할 수 있지만, 생각하는대로 되지 않는 경우가 많다.