import cv2

#1.获取视频
cap = cv2.VideoCapture(0)

if __name__ == "__main__":
    while True:

        #2.获取每一帧的的图片
        if cap.isOpened():#用来判断摄像头是否真正的运行起来
            ret, frame = cap.read()
        else:
            break
        #3.装灰度化
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        #4.显示灰度图片
        cv2.imshow("gray",gray)

        #5.随时终止数据
        if cv2.waitKey(1) and 0xff == ord('c'):
            break

    #6.释放摄像头
    cap.release()
    cv2.destroyAllWindows()