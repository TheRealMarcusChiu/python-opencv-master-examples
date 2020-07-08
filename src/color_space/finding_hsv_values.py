import numpy as np
import cv2 as cv

green = np.uint8([[[0, 255, 0]]])
hsv_green = cv.cvtColor(green, cv.COLOR_BGR2HSV)
print(hsv_green)
# [[[ 60 255 255]]]

# Now you take [H-10, 100,100] and [H+10, 255, 255] as the lower bound and upper bound respectively
