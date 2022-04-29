import cv2 as cv

vid = cv.VideoCapture(0)


def changeRes(width, height):

    vid.set(3, width)
    vid.set(4, height)


width = input('Set width: ')
height = input('Set height: ')
changeRes(width=int(width), height=int(height))

while True:

    ret, frame = vid.read()
    cv.imshow('Frame', frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()