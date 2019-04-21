import cv2

#打开摄像头

cap = cv2.VideoCapture(0)

while 1:

    ret, frame = cap.read()
    """
    cap.read()按帧读取视频，ret,frame是获cap.read()
    方法的两个返回值。其中ret是布尔值，如果读取帧是正确的则返回True，
    如果文件读取到结尾，它的返回值就为False。frame就是每一帧的图像，是个三维矩阵。
    """
    cv2.imshow("Video", frame)
    c = cv2.waitKey(0)
    if c == 27:
        break

    #释放摄像头
    cap.release()
    #关闭所有窗口
    cv2.destroyAllWindows()