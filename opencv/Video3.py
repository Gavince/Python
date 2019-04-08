import cv2

cap = cv2.VideoCapture("/home/gavin/Desktop/video/1.0")

fps = cap.get(cv2.CAP_PROP_FPS)
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

print("fps=",fps,"frame=",frames)

for i in range(int(frames)):
    ret, frame = cap.read()
    cv2.imwrite("/home/gavin/Paper",frame)