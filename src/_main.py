import cv2 as cv

print("OpenCV version:")
print(cv.__version__)

img = cv.imread("../data/clouds.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Over the Clouds", img)
cv.imshow("Over the Clouds - gray", gray)

cv.waitKey(0)
cv.destroyAllWindows()
