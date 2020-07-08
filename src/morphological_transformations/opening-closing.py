import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_opening = cv.imread('../../data/j-opening.png', 0)
img_closing = cv.imread('../../data/j-closing.png', 0)
kernel = np.ones((11, 11), np.uint8)
# OPENING - erosion followed by dilation
opening = cv.morphologyEx(img_opening, cv.MORPH_OPEN, kernel)
# CLOSING - dilation followed by erosion
closing = cv.morphologyEx(img_closing, cv.MORPH_CLOSE, kernel)

titles = ['Image 1 - Original', 'Image 1 - OPENING',
          'Image 2 - Original', 'Image 2 - CLOSING']
images = [img_opening, opening,
          img_closing, closing]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
