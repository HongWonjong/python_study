import numpy as np
def sum_squares_error(y, t):
    return 0.5 * np.sum((y - t)**2)

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] 
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0] # 2일 확률이 가장 높다고 추정
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0] # 7일 확률이 가장 높다고 추정
a = sum_squares_error(np.array(y), np.array(t))
b = sum_squares_error(np.array(y2), np.array(t))
print(a)
print(b)

# 오차제곱합은 y2보다 y에서 더 작으므로, y가 정답에 더 가까울 것이라고 판단할 수 있다.