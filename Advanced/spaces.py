import cv2 as cv

img = cv.imread("/Users/thomas.greiner/PycharmProjects/computer_vision/Advanced/Photos/roses.jpeg")
cv.imshow('Roses', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to lab
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('lab', lab)


cv.waitKey(0)