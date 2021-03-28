# 유닉스 타임이란 세계 표준시로, 1970년 1월 1일 0시 0분 0초를 기준으로 몇 초가
# 지났는지를 정수로 나타낸 것을 말합니다. 파이썬에서 유닉스 타임을 구할때는 
# 다음의 코드를 사용한다.

import time

# 변수를 선언한다.

number = 0

# 5초 동안 반복한다.
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

print("5초 동안 {}번 반복했습니다.".format(number))