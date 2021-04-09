import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

def f(x0, x1):
    return x0**2 + x1**2

#x0, x1를 계산할 범위를 설정해준다. 구간을 -2 ~ 2로 설정하고, 20등분 해준다.
xn = 20
x0 = np.linspace(-2, 2, xn)
x1 = np.linspace(-2, 2, xn)
#print(x0)  # 리스트에 각 숫자들이 저장된 것을 볼 수 있다.
#print(x1)

# x0, x1의 각 값들을 함수에 집어넣었을 때의 결과값을 저장하기 위해 2차원 배열 temp를 지정해주자.
tmp = np.zeros((len(x0), len(x1)))   # 2차원 배열변수 temp의 각 요소들을 0으로 초기화하고, 0차원의 길이를 x0 요소의 개수만큼, 1차원의 길이를 x1 요소의 개수만큼으로 정했다.

# 이제 temp에 x0, x1가 함수에 들어갔을 때 함수의 출력값을 넣어주자.
for i in range(xn):
    for j in range(xn):
        tmp[i, j] = f(x0[i], x1[j])

# print(tmp) # 이렇게 출력하는게 보통이겠지만, 이런 방법은 어떨까?
# print(np.round(tmp, 1)) # 이렇게 출력하면 빈칸들을 없애줘서 출력 결과를 시각화 하기가 좋다.

# 우선 진짜 3차원 그래프 말고, 색깔로 출력 결과를 표시하는 3차원 조무사 그래프도 그려보자.

# plt.gray() # 색상을 회색 음영으로 표현하도록 지정
# plt.pcolor(tmp) # pcolor기능을 통해 행렬을 색상으로 나타냄
# plt.colorbar() # 옆에 컬러바를 나타냄
# plt.show()

# 우선 좌표점 x0, x1을 통해 좌표점 x0x0, x1x1을 만들 것이다.
x0x0, x1x1 = np.meshgrid(x0, x1)
# 이 둘은 각각 tmp 배열과 크기가 같은 2차원 배열이다.

# 이제 차트를 3차원으로 설정해보자.
ax = plt.subplot(1, 1, 1, projection = '3d') # ax를 선언하여 그래프의 id를 저장하고, 차트를 3차원으로 만들어준다.

# 함수의 표면을 그래프에 표시해보자.
ax.plot_surface(x0x0, x1x1, tmp, rstride = 5, cstride = 5, alpha = 0.3, color = 'blue', edgecolor = 'black')
# cstride, rstride는 몇 번째 등분마다 선을 표시할 지 정한다. 수가 크면 그래프가 좀 보기 좋다.
ax.view_init(75, -95)  # 보는 관점을 지정해준다. 매개변수 1은 상하회전 각도(0~90, 0은 옆에서 본 각도, 90은 위에서 본 각도), 매개변수 2는 좌우회전 각도(양수-시계방향으로 회전, 음수-반시계로 회전)
plt.show()

