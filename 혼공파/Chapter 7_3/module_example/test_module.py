PI = 3.141592

def number_input():
    output = input("숫자 입력>")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius

# 이 코드에 __name__을 이용한 조건문을 쓰지 않으면, 모듈에서의 출력이
# 실제 메인 파일에서도 출력되어버리는 문제가 생긴다.
if __name__ == "__main__":
    print("get_circumference(10):", get_circumference(10))
    print("get_circle_area(10):", get_circle_area(10))
