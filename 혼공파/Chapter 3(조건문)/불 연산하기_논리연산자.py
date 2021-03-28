# 불끼리는 논리 연산자를 사용할 수 있다. 파이썬에는 다음과 같은 논리 연산자가 있다. not, and, or

#not: 아니다라는 의미, 불을 반대로 전환한다. 피연산자가 1개이기 때문에 "단항연산자"이다.
print(not True)

print(not False)

#not연산자 활용해보기
x = 50
under_20 = x < 20
print("under_20:", under_20)

#and 연산자와 or 연산자 활용해보기
#and 연산자는 양쪽 변의 값이 모두 참일때만 결과값을 True로 낸다.
print(True and True)
print(False and False)

#반면 or 연산자는 양 변의 값 중 하나만 참이어도 결과값을 True로 낸다.
print(True or False)
print(True or True)