str_a = input("문자열 입력>")
str_b = input("문자열 입력>")

print(str_a, str_b)

str_c = str_a
str_a = str_b
str_b = str_c
print(str_a, str_b)
