import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)

while 1:
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    blur = cv.GaussianBlur(frame, (9, 9), 0)
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([140, 255, 255])
    # for tracking other colors see finding_hsv_values.py

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
