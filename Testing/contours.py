import cv2 as cv
import numpy as np

img = cv.imread('Photos/roses.jpeg')
cv.imshow('Original', img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

blur = cv.GaussianBlur(gray, (9, 9), sigmaX=2, sigmaY=2, borderType=cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

# edge detector with canny
canny = cv.Canny(blur, 125, 175)
cv.imshow("canny", canny)

# edge detection with binary
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("thresh", thresh)

# get contours
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours(s) found!')

cv.drawContours(blank, contours, -11, (0, 0, 255), 1)
cv.imshow('contours drawn', blank)


cv.waitKey(0)