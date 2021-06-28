# 나쁜 예

def numerical_diff(f, x):
    h = 10e-50
    return (f(x + h) - f(x)) / h  # 여기서는 전방 차분을 이용한다.
x = 2.0
def function(x):
    return 2*x +1
a = numerical_diff(function, x)

print(a)
# delta 값을 너무 작게 설정했기에 컴퓨터 상에서 0.0으로 출력 해버리고 만다. 따라서 결과가 좋게 나온다고 알려지는 h = 10e-4를 입력해보자.

# 좋은 예(첫 번째 개선 방법)
def n_d(f, x):
    h = 10e-4
    return (f(x + h) - f(x)) / h  # 여기서는 전방 차분을 이용한다.
b = n_d(function, x)

print(b)

# 이제 전방 차분을 중심 차분(중앙 차분)으로 바꿔서 수치 미분을 다시 구현해보자.
def numerical_d(f, x):
    h = 10e-4
    return (f(x+h) - f(x-h)) / 2*h

c = numerical_d(function, x)
print(c)