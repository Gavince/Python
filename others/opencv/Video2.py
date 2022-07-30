import cv2
import numpy as np

#open video
cap = cv2.VideoCapture(0)

#读取数据
while(1):

    # get a frame
    ret, frame = cap.read()
    #show a frame
    cv2.imshow("Capture", frame)

    if cv2.waitKey(0) and 0xff == ord('c'):
        break

    cap.release()
    cv2.destroyAllWindows()