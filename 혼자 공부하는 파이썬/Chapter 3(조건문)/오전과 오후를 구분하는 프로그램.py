import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.".format(now.hour))
if now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다.".format(now.hour))

if 3 <= now.month <= 5:
    print("이번 달은 {}월이며 봄입니다.".format(now.month))

if 6 <= now.month <= 8:
    print("이번 달은 {}월이며 여름입니다.".format(now.month))

if 9 <= now.month <= 11:
    print("이번 달은 {}월이며 가을입니다.".format(now.month))
#정수형인데 어떻게 12보다 크고 2보다 작냐;;
if now.month == 12 or now.month <= 2:
    print("이번 달은 {}월이며 겨울입니다.".format(now.month))