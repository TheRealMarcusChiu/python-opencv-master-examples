import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# - black-to-white transition is taken as positive slope (it has a positive value)
# - white-to-black transition is taken as negative slope (it has negative value)
# So when you convert data to np.uint8, all negative slopes are made zero
# In simple words, you miss that edge

img = cv.imread('../../data/black.jpg', 0)

# Output dtype = cv.CV_8U
sobelx8u = cv.Sobel(img, cv.CV_8U, 1, 0, ksize=5)

# Output dtype = cv.CV_64F. Then take its absolute and convert to cv.CV_8U
sobelx64f = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

images = [img, sobelx8u, sobel_8u]
titles = ['Original', 'Sobel CV_8U', 'Sobel abs(CV_64F)']

for i in range(3):
    plt.subplot(3, 1, i + 1), plt.imshow(images[i], cmap='gray')
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])

plt.show()
