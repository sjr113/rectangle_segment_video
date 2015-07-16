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

image_segment_data = []
image_segment_label = []

frame_number = 0
img2 = zeros((width, width), uint8)
play = True
next_position = cap.get(1)
while True:
    print next_position
    if success:
        frame_number += 1
        success, frame = cap.read(next_position)
        next_position += 1
        dst = cv2.cvtColor(frame, cv2. COLOR_BGR2GRAY)
        dst2 = array(dst)
# dst2 = dst2.reshape(1920, 1080)
        a = int(width * 0.6)
        b = width - a

        img2 = dst2[(iy - a):(iy + b), ix:(ix + width)]
        image_segment_data.append(img2)
        image_segment_label.append(-1)
# image = cap.get()
        if frame_number < 5:
            filename = str(frame_number) + ".jpg"
            cv2.imwrite(filename, img2)
        cv2.rectangle(frame, (ix, iy - a), (ix + width, iy + b), (0, 255, 0), 0)
        cv2.imshow('video', frame)

        if play is True:
            key_number = cv2.waitKey(35)
            if key_number == 27:
                break
            elif key_number == 32:  # the video is stopped when push Space key
                play = False
            else:
                pass
        else:
            key_number2 = cv2.waitKey(0) & 0xFF
            if key_number2 == 27:
                break
            elif key_number2 == ord("e"):   # push the top key to the prior frame
                print "-----"
                print next_position
                print "------"
                next_position -= 1
                if next_position < 0:
                    cap.set(1, 0)
                else:
                    cap.set(1, next_position)
            elif key_number2 == ord("x"):
                next_position -= 1
                if next_position < 0:
                    cap.set(1, 0)
                else:
                    cap.set(1, next_position)
            elif key_number2 == 9:
                play = True
            else:
                play = False

print shape(image_segment_data)
print image_segment_label
cv2.destroyAllWindows()
# cv2.resize(img, (40, 40), interpolation=cv2.INTER_CUBIC)
# cv2.namedWindow("image_segment")
# cv2.imshow('image_segment', image_segment_data[0])
# cv2.waitKey(0)

