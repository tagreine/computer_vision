import cv2 as cv

img = cv.imread('Photos/roses.jpeg')

blur = cv.GaussianBlur(img, ksize=(9,9), sigmaX=3, sigmaY=3, borderType=cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

canny = cv.Canny(blur, threshold1=100, threshold2=200)
cv.imshow("Canny edges", canny) # pass in either blur or img

dilated = cv.dilate(canny, kernel=(7,7), iterations=10)
cv.imshow("dilated canny", dilated)

eroded = cv.erode(dilated, kernel=(7,7), iterations=5)
cv.imshow("eroded", eroded)

resized = cv.resize(img, dsize=(2000, 1000), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

cv.waitKey(0)