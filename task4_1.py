from ultralytics import YOLO

# 1. 加载官方预训练模型（第一次运行会自动下载一个几MB的文件，稍微等几秒）
print("正在加载 YOLO 模型...")
model = YOLO('yolov8n.pt') 

# 2. 对之前的 test.jpg 进行推理
print("正在识别图片...")
results = model('test.jpg')

# 3. 把识别结果保存下来，会自动画上框和标签
for r in results:
    r.save(filename='task4_yolo_result.jpg')

print("识别完成！结果已保存为 task4_yolo_result.jpg")