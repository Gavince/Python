import cv2 as cv

if __name__ == '__main__':
    src = cv.imread("/home/gavin/Downloads/5.jpg")
    cv.imshow("src", src)

    hog = cv.HOGDescriptor()
    hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())
    (rects, weights) = hog.detectMultiScale(src, winStride=(4,4), padding=(8, 8), scale=1.3, useMeanshiftGrouping=False)

    for (x, y, w, h) in rects:

        cv.rectangle(src, (x,y), (x+w, y+h),(255,0,0),2)

    cv.imshow("Hog_detector", src)
    cv.waitKey(0)
    cv.destroyAllWindows()