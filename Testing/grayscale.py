import cv2 as cv

#print(os.getcwd())
img = cv.imread('Photos/roses.jpeg')

gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow("roses", gray)

blur = cv.GaussianBlur(img, ksize=(9,9), sigmaX=3, sigmaY=3, borderType=cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

canny = cv.Canny(img, threshold1=100, threshold2=200)
cv.imshow("Canny edges", canny)

cv.waitKey(0)