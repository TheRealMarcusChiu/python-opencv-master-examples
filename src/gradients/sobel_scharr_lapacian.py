import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../../data/sudoku.png', cv.IMREAD_GRAYSCALE)
laplacian = cv.Laplacian(img, cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)

images = [img, laplacian, sobelx, sobely]
titles = ['Original', 'Lapacian', 'Sobel X', 'Sobel Y']

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], cmap='gray')
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])

plt.show()
