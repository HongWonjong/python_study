numbers = [5,15,6,20,7,25]

for number in numbers:  
    if number < 10:
        continue
    print(number)

# continue 이후에 진행시키고자 하는 구문은 continue보다 앞에 와 있어야 한다.

for i in range(3, 9+1, 3):
    print(i)