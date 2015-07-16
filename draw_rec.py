__author__ = 'shen'
__author__ = 'shen'
# ch010_20150625092943.avi

import cv2
# import numpy as np


def draw_rectangle(event, x, y, flags, param):
    global drawing, ix, iy, width
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing is True:
            img = frame.copy()
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 0)
            cv2.imshow('video', img)
    elif event == cv2.EVENT_LBUTTONUP:
        width = x - ix
        drawing = False


cap = cv2.VideoCapture("E:\\ch010_20150625092943.avi")
# fps = cap.get(cv2.CV_CAP_PROP_FPS)
cv2.namedWindow("video")

success, frame = cap.read()
drawing = False
ix = -1
iy = -1
width = -1
cv2.setMouseCallback("video", draw_rectangle)
cv2.imshow("video", frame)

while success:
    if (cv2.waitKey(33)) == 27:  # When push the "esc", the video begain
        break


# print ix, iy, width


