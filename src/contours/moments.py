import cv2 as cv

img = cv.imread('../../data/star.jpg', 0)
ret, thresh = cv.threshold(img, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv.moments(cnt)
print(M)
