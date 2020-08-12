from __future__ import absolute_import, division, print_function, unicode_literals

import cv2
import math

im1 = cv2.imread('1.png',cv2.IMREAD_GRAYSCALE)
im2 = cv2.imread('2.png',cv2.IMREAD_GRAYSCALE)
im4 = cv2.imread('4.png', cv2.IMREAD_GRAYSCALE)

# two images (im1 and im2) are similar if the above distances are small
d11 = cv2.matchShapes(im1,im2,cv2.CONTOURS_MATCH_I1,0)
d21 = cv2.matchShapes(im1,im4,cv2.CONTOURS_MATCH_I1,0)

print('CONTOURS_MATCH_I1 (im1 vs im2): ', d11)
print('CONTOURS_MATCH_I1 (im1 vs im4): ', d21)

# other contours_match
d12 = cv2.matchShapes(im1,im2,cv2.CONTOURS_MATCH_I2,0)
d13 = cv2.matchShapes(im1,im2,cv2.CONTOURS_MATCH_I3,0)