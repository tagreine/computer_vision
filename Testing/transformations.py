import cv2 as cv
import numpy as np

img = cv.imread('Photos/roses.jpeg')


def translate(img, x, y):
    transMat = np.float([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

