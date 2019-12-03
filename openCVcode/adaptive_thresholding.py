# adaptivee thresholding give us better result for images with variyng eliminations

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img= cv.imread('../images/butterfly.jpg',False)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,15, 2)


titles = ['Orginal picture','THRESH_BINARY', 'ADAPTIVE_THRESH_MEAN_C','ADAPTIVE_THRESH_GAUSSIAN_C']
images = [img,th1, th2, th3]
for i in range(4):
    plt.subplot(2,2,i+1),
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),
    plt.yticks([])

plt.show()

# cv.imshow("Image", img)
# cv.imshow("th1", th1)vlear
