import numpy as np 
# 기울기 구현
def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x) # 입력된 매개변수 x와 형상이 같은 배열을 생성
    
    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h)계산
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h)계산
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 값 복원
    return grad

def function_2(x):  # 기울기 함수의 매개변수에 넣을 함수를 선언
    return x[0] **2 + x[1] **2

grad = numerical_gradient(function_2, np.array([3.0, 4.0]))
print(grad)
# 이렇게 (x0, x1)각 점에서의 기울기를 계산할 수 있다. 그런데 이 기울기는 무엇을 의미할까?