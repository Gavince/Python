import cv2

#1.读取视频数据
cap = cv2.VideoCapture("/home/gavin/Desktop/video/2.mp4")

#2.处理数据
while True:

    #读取每一帧的数据
    ret, frame = cap.read()
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    (rects, weights) = hog.detectMultiScale(frame, winStride=(4,4), padding=(8, 8), scale=1.05, useMeanshiftGrouping=False)
    for (x, y, w, h) in rects:

        cv2.rectangle(frame, (x,y), (x+w, y+h),(255,0,0),2)

    cv2.imshow("Hog_detector", frame)
    cv2.waitKey(1)
