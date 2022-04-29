import cv2 as cv

vid = cv.VideoCapture(0)


def rescaleFrame(frame, scale=0.75):
    """
    Rescaling images, video or live video
    :param frame: image frame from image or video
    :param scale: scaling percentage passed to a integer
    :return: the resized frame
    """
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

scale = input('Set scale: ')

while True:

    ret, frame = vid.read()
    frame_resize = rescaleFrame(frame=frame, scale=float(scale))
    cv.imshow('Frame', frame_resize)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()