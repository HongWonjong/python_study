import numpy as np

def cross_entropy_error(y, t):
    delta = 1e-7 # y에 델타를 더해주는 이유는, y가 아예 0일때는 np.log()의 값이 마이너스 무한대를 뜻하는 -inf가 되기 때문이다. 그래서 델타라는 아주 작은 값을 더해준다.
    return -np.sum(t * np.log(y + delta)) # 여기서 y와 t는 넘파이 배열이다.

# 이제 오차제곱합 때와 똑같은 출력값과 참값을 가져와서 교차 엔트로피 오차를 구해보자.
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] 
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0] # 2일 확률이 가장 높다고 추정
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0] # 7일 확률이 가장 높다고 추정

a = cross_entropy_error(np.array(y), np.array(t))
b = cross_entropy_error(np.array(y2), np.array(t))

print(a, b)

# y의 오자체곱합이 0에 더 가까우므로 첫 번째 추정이 정답일 확률이 높다는 것을 알 수 있다. 이는 오자제곱합의 판단과 일치한다.