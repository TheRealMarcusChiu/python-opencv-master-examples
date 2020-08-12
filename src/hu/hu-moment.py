from __future__ import absolute_import, division, print_function, unicode_literals

import cv2
import math


def return_hu_moments(filename):
    # get image
    im = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    # Binarize the image using thresholding
    _,im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)

    # Calculate Moments
    moments = cv2.moments(im)
    # Calculate Hu Moments
    huMoments = cv2.HuMoments(moments)

    # Log scale hu moments
    for i in range(0,7):
        huMoments[i] = -1 * math.copysign(1.0, huMoments[i]) * math.log10(abs(huMoments[i]))

    return huMoments


hm1 = return_hu_moments('1.png')
hm2 = return_hu_moments('2.png')
hm3 = return_hu_moments('3.png')

for i in range(0,7):
    print(hm1[i], "\t", hm2[i], "\t", hm3[i])
