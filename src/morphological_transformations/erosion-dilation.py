import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../../data/j.png', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)
dilation = cv.dilate(img, kernel, iterations=1)

titles = ['Original Image', 'EROSION', 'DILATION']
images = [img, erosion, dilation]

for i in range(3):
    plt.subplot(1, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
