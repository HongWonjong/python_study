# 실수를 소수점 몇 번째 자리까지 나타낼지 .x로 정해줄 수 있다.
output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273)
#의미없는 소수점을 없애고 싶을 때
output_d = "{:15g}".format(52.0)
print(output_a)
print(output_b)
print(output_c)
print(output_d)
