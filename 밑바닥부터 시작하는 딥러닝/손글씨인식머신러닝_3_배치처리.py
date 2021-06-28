import numpy as np
from mnist import load_mnist
import PIL
from PIL import Image
import pickle

def get_data():
    (x_train, t_train),(x_test, t_test) = \
    load_mnist(flatten = True, normalize = False)
    return x_test, t_test

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) +b3
    y = softmax(a3)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

# 이제 선언한 함수들로 추론을 수행해보자.

x, t = get_data()
network = init_network()
batch_size = 100 # 배치 크기
accuracy_cnt = 0
for i in range(0, len(x), batch_size):
    x_batch = x[i:i + batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis = 0) # 확률(최댓값)이 가장 높은 원소의 인덱스를 p에 저장한다. 이번에는 axis = 0이라는 매개변수가 추가되었는데, 이는 100 * 10의 배열 중 0번째 차원을 구성하는 각 원소에서(0번째 차원을 축으로, 즉 row를 기준으로) 최댓값의 인덱스를 찾도록 한 것이다.
    accuracy_cnt += np.sum(p == t[i:i+batch_size]) # 참이라면 True는 np.sum()함수에서 1로 변환되어 더해진다.
print("Accuracy:" + str(float(accuracy_cnt)/len(x)))