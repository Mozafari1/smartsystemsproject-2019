# morphological transformations are some simple operations based on the image shape
# This transformations are normally performed onbinary images

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
img = cv.imread("../images/smarties.png", cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
# A kernel is a shape or squre we apply on images
# Dilation will remove the black dots from images in mask image

dilation  = cv.dilate(mask, kernel=np.ones((3,3), np.uint8), iterations=4)
erosion = cv.erode(mask, kernel=np.ones((2,2), np.uint8), iterations=2)
gradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel=np.ones((2,2),np.uint8))
# there are some more morphollogical transformations

title = ["image", "mask", "dilation", "erosion", "gradient"]
image = [img, mask, dilation, erosion, gradient]

for i in range (5):
    plt.subplot(2, 3, i+1),
    plt.imshow(image[i], 'gray')
    plt.title(title[i])
    plt.xticks([]),
    plt.yticks([])

plt.show()

