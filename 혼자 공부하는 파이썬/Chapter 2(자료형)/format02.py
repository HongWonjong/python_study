#{:d}를 사용한 경우 매개변수로 int 자료형의 정수만 올 수 있다.
output_a = "{:d}".format(52)
print(output_a)

# 특정 칸에 출력하는 방법
output_a = "{:5d}".format(52)
print(output_a)

#빈 칸을 0으로 채우려면 이렇게 입력하자.
output_a = "{:05d}".format(52)
print(output_a)

output_a = "{:05d}".format(-52)
print(output_a)