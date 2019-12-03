# Conturs is a python list offf all the contours in the image.
#Each individual contour is a numpy array of (x,y) coordinates of boundary points of obejcts

import cv2 as cv 
import numpy as np 

img = cv.imread("../images/opencv-logo.png")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold  (imgray,130, 255, False)
contours, hierarchy  = cv.findContours(thresh, cv.RETR_TREE,cv.CHAIN_APPROX_NONE )
print("Number of contours = "+ str(len(contours)))

cv.drawContours(img, contours, -1, (255,255, 0), 4)
cv.imshow('Original', img)
cv.imshow('Gray', imgray)
cv.waitKey(False)
cv.destroyAllWindows()
