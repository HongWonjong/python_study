# 미니배치 같은 배치 데이터를 지원하는 교차 엔트로피 오차는 어떻게 구현할까? 데이터가 하나인 경우와 데이터가 배치로 묶여 입력될 경우 모두를 처리할 수 있도록 구현해보자.

import numpy as np

def cross_entropy_error(y, t):
    delta = 1e-7 # y에 델타를 더해주는 이유는, y가 아예 0일때는 np.log()의 값이 마이너스 무한대를 뜻하는 -inf가 되기 때문이다. 그래서 델타라는 아주 작은 값을 더해준다.
    return -np.sum(t * np.log(y + delta)) # 여기서 y와 t는 넘파이 배열이다.