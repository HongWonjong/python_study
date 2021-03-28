max_value = 0
a = 0
b = 0

for i in range(100):
    j = 100-i
    #최댓값 구하기
    
    if a*b < i*j:
        a = i
        b = j
        max_value = a * b
    



print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))