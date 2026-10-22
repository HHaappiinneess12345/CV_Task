import cv2

# 1. 读取图片
img = cv2.imread('test.jpg')
if img is None:
    print("错误：找不到 test.jpg")
else:
    # 2. 转灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 3. 二值化处理（把图片变成纯黑纯白，方便找轮廓）
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # 4. 寻找轮廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 5. 在原图上画出轮廓
    result_img = img.copy()
    # 绿色画轮廓，线宽为 2
    cv2.drawContours(result_img, contours, -1, (0, 255, 0), 2)

    # 6. 计算总面积和总周长
    total_area = 0
    total_perimeter = 0
    for cnt in contours:
        total_area += cv2.contourArea(cnt)
        total_perimeter += cv2.arcLength(cnt, True)

    # 打印结果
    print(f"检测到的轮廓数量: {len(contours)}")
    print(f"轮廓的总面积: {total_area:.2f}")
    print(f"轮廓的总周长: {total_perimeter:.2f}")

    # 7. 保存画了轮廓的图片
    cv2.imwrite('task2_3_result.png', result_img)
    print("包含轮廓的图片已保存为 task2_3_result.png")