
def numerical_diff(f, x):
    h = 10e-4
    return (f(x+h) - f(x-h)) / 2*h

def function_2(x0, x1):
    return x0**2 + x1**2
# x0 = 3이고 x1 = 4일 때 각 각의 변수에 대한 편미분을 구현해보자.
def function_tmp1(x0): # x1의 값이 4로 고정되어 있을 때(변수를 상수화 시켰을 때) x0 = 3.0인 순간 f(x0)의 x0에 대한 변화량을 구하는 식
    return x0**2 + 4.0**2

def function_tmp2(x1):
    return 3**2 + x1**2  # x0이 3일 때 """
a = numerical_diff(function_tmp1, 3.0)
b = numerical_diff(function_tmp2, 4.0)
print(a)
print(b)
