import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread('test.jpg')
if img is None:
    print("错误：找不到 test.jpg")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rows, cols = img.shape[:2]

    # 1. 缩放
    img_scaled = cv2.resize(img, (cols // 2, rows // 2))

    # 2. 旋转
    M_rot = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    img_rotated = cv2.warpAffine(img, M_rot, (cols, rows))

    # 3. 平移
    M_trans = np.float32([[1, 0, 50], [0, 1, 50]])
    img_translated = cv2.warpAffine(img, M_trans, (cols, rows))

    # 4. 翻转
    img_flipped = cv2.flip(img, 1)

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 3, 1)
    plt.title('Original')
    plt.imshow(img)
    plt.axis('off')

    plt.subplot(2, 3, 2)
    plt.title('Scaled (0.5x)')
    plt.imshow(img_scaled)
    plt.axis('off')

    plt.subplot(2, 3, 3)
    plt.title('Rotated 45 deg')
    plt.imshow(img_rotated)
    plt.axis('off')

    plt.subplot(2, 3, 4)
    plt.title('Translated')
    plt.imshow(img_translated)
    plt.axis('off')

    plt.subplot(2, 3, 5)
    plt.title('Flipped')
    plt.imshow(img_flipped)
    plt.axis('off')

    plt.tight_layout()
    
    # 重点在这里：直接保存图片，不弹窗了
    plt.savefig('task2_2_result.png')
    print("图片已保存为 task2_2_result.png")