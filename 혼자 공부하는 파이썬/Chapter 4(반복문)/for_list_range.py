# 지금 반복되서 출력되고 있는 문장이 몇 번째 반복에서 비롯된 것인지를 알고 싶다면......

array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))