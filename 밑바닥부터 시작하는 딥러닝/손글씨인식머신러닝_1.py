
import numpy as np
from mnist import load_mnist
import PIL
from PIL import Image

def img_show(img):
       pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train),(x_test, t_test) = \
    load_mnist(flatten = True, normalize = False)

img = x_train[0]
label = x_train[0]
print(label)  #5

print(img.shape)
img = img.reshape(28, 28) # 넘파이 배열화 되어있는 데이터를 원래 이미지의 모양으로 변환
print(img.shape)

img_show(img)