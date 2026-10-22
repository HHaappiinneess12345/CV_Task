import cv2
from PIL import Image
import matplotlib.pyplot as plt

# 1. 用 OpenCV 读取图片
img_cv = cv2.imread('test.jpg')
if img_cv is None:
    print("错误：找不到 test.jpg，请检查图片名字和路径！")
else:
    # 2. 用 Pillow 读取图片并显示
    img_pil = Image.open('test.jpg')
    img_pil.show(title="Pillow 显示原图")

    # 3. 分离三个通道 (OpenCV 默认是 BGR 格式)
    b, g, r = cv2.split(img_cv)
    
    # 把 BGR 转为 RGB 用于 matplotlib 正常显示颜色
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

    # 4. 使用 matplotlib 画出原图和三个单通道
    plt.figure(figsize=(10, 8))
    
    plt.subplot(2, 2, 1)
    plt.title('Original Image')
    plt.imshow(img_rgb)
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.title('Blue Channel')
    plt.imshow(b, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.title('Green Channel')
    plt.imshow(g, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.title('Red Channel')
    plt.imshow(r, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()