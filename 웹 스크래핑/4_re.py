import re


def print_match(m):
    if m:
        print("m.group():", m.group())   # group은 일치하면 일치하는 문자열을 반환
        print("m.string():", m.string) # string은 일치하면 입력받은 문자열을 그대로 반환
        print("m.start():", m.start())
        print("m.end():", m.end())
        print("m.span():", m.span())
    else:
        print("매칭되지 않았습니다.")
p = re.compile("ca.e") 
m = p.match("careless")   # match()함수는 주어진 문장의 처음부터 일치하는지를 확인하기 때문에, careless의 뒷부분은 상관이 없다.
f = p.match("lesscare")   # 처음부분이 일치하지 않으므로 뒷 부분이 일치하더라도 상관이 없다.
#print_match(m)
#print_match(f)

m = p.search("goodcare")
print_match(m)

lst = p.findall("care cave cafe cape")
print(lst)