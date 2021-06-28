import numpy as np 

def numerical_gradient(f, x):   # 기울기를 구하는 함수
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


def gradient_descent(f, init_x, lr = 0.01, step_num = 100):  # 경사하강법 구현 함수
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x

def function(x): # 기울기를 구할 함수, 초깃값은 (-3.0, 4.0)으로 설정하자.
    return x[0]**2 + x[1] **2

a = gradient_descent(function, np.array([-3.0, 4.0]), lr = 0.1, step_num = 100)

print(a)
