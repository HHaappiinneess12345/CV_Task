import cv2
import numpy as np

# 读取 example2.mp4
cap = cv2.VideoCapture('example2.mp4')
if not cap.isOpened():
    print("错误：打不开 example2.mp4，请检查视频名字对不对！")
else:
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # 左右拼接，宽度是原来的2倍
    out = cv2.VideoWriter('task2_4_result.mp4', fourcc, fps, (width * 2, height))

    mog2 = cv2.createBackgroundSubtractorMOG2()

    print("正在处理视频，按 'ESC' 键可以提前退出...")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        fgmask = mog2.apply(frame)
        fgmask_bgr = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR)
        
        combined = np.hstack((frame, fgmask_bgr))
        
        out.write(combined)
        cv2.imshow('Original vs MOG2', combined)
        
        if cv2.waitKey(30) & 0xFF == 27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("处理完成！已保存为 task2_4_result.mp4")