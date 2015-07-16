__author__ = 'shen'

import cv2
from numpy import *
# import draw_rec
# ix = draw_rec.ix
# iy = draw_rec.iy
# width = draw_rec.width
ix = 1194
iy = 298
width = 95

cap = cv2.VideoCapture("E:\\ch010_20150625092943.avi")
# fps = cap.get(cv2.CV_CAP_PROP_FPS)
cv2.namedWindow("video")
success, frame = cap.read()



n = 0
img2 = zeros((width, width), uint8)
while success:
    n += 1
    success, frame = cap.read()
    dst = cv2.cvtColor(frame, cv2. COLOR_BGR2GRAY)
    dst2 = array(dst)
# dst2 = dst2.reshape(1920, 1080)
    a = int(width * 0.6)
    b = width - a
    img2 = dst2[(iy - a):(iy + b), ix:(ix + width)]
    if n < 5:
        filename = str(n) + ".jpg"
        cv2.imwrite(filename, img2)
    cv2.rectangle(frame, (ix, iy - a), (ix + width, iy + b), (0, 255, 0), 0)
    cv2.imshow('video', frame)
    if (cv2.waitKey(33)) == 27:  # When push the "space", the video begain
        break
    success, frame = cap.read()

