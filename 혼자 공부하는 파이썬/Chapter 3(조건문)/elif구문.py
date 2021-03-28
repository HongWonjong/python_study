import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("지금은 봄입니다.")
elif 6 <= month <= 8:
    print("지금은 여름입니다.")
elif 9<= month <= 11:
    print("지금은 가을입니다.")
else:
    print("지금은 겨울입니다.")
