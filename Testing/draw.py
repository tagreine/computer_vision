import cv2 as cv
import numpy as np

# create a blank image (data type = uint8)
blank = np.zeros([500, 500, 3], dtype='uint8')

#cv.imshow('blank', blank)
#blank[:] = 0, 255, 0
#cv.imshow('green', blank)

cv.rectangle(blank, pt1=(0,0), pt2=(250, 250), color=(0,0,255), thickness=2)
cv.imshow("rectangle", blank)

cv.circle(blank, center=(blank.shape[1]//2, blank.shape[0]//2), radius=40, color=(0, 255, 0), thickness=2 )
cv.imshow("circle", blank)

cv.line(blank, pt1=(0, 0), pt2=(250, 250), color=(255, 255, 255), thickness=2)
cv.imshow("line", blank)

cv.putText(blank, org=(170, 250), text="Hello blank", fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=(255, 0, 0),thickness=2)
cv.imshow("text", blank)

cv.waitKey(0)