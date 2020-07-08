import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

cv.samples.addSamplesDataSearchPath("../../data")

img = cv.imread(cv.samples.findFile("starry_night.jpg"))
# imread() reads in BGR order, so convert to RGB
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25

img_edges = cv.Canny(img, 100, 200)

img_blurred = cv.filter2D(img, -1, kernel)
img_blurred_edges = cv.Canny(img_blurred, 100, 200)

img_guassian = cv.GaussianBlur(img, (5, 5), 0)
img_guassian_edges = cv.Canny(img_guassian, 100, 200)

img_bilateral = cv.bilateralFilter(img, 9, 75, 75)
img_bilateral_edges = cv.Canny(img_bilateral, 100, 200)


# display images
f, axarr = plt.subplots(2, 4)
axarr[0, 0].imshow(img)
axarr[0, 0].set_title('IMG')
axarr[1, 0].imshow(img_edges)
axarr[1, 0].set_title('IMG EDGES')

axarr[0, 1].imshow(img_blurred)
axarr[0, 1].set_title('BLURRED ')
axarr[1, 1].imshow(img_blurred_edges)
axarr[1, 1].set_title('BLURRED EDGES')

axarr[0, 2].imshow(img_guassian)
axarr[0, 2].set_title('GUASSIAN')
axarr[1, 2].imshow(img_guassian_edges)
axarr[1, 2].set_title('GUASSIAN EDGES')

axarr[0, 3].imshow(img_bilateral)
axarr[0, 3].set_title('BILATERAL')
axarr[1, 3].imshow(img_bilateral_edges)
axarr[1, 3].set_title('BILATERAL EDGES')

plt.show()

# imshow displays in BGR order
# cv.imshow("IMAGE", img)
