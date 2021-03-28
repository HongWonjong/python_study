# 컴퓨터에게 반복하여 어떤 명령을 지시해보자.
# for 반복문의 구조는 대략 이렇다.
# for 반복자 in 반복할 수 있는 것:
# 코드

# "반복할 수 있는 것"이란 문자열, 리스트, 딕셔너리, 범위 등이 있다.

array = [273, 32, 103, 57, 52]

# 158페이지 3번 예제의 연습도 해보자.
for element in array:
    if len(str(element)) == 1:
        print("{}는 한 자릿수입니다.".format(element))  
    elif len(str(element)) == 2:
        print("{}는 두 자릿수입니다.".format(element))
    else :
        print("{}는 세 자릿수입니다.".format(element))

# range(100)과 같은 범위 자료형은 for 반복문과 많이 함께 사용되고, 출력을 반복한다.