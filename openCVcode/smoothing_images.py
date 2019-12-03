import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread("../images/me.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/20
destination = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (5,5))
gaussianblur = cv.GaussianBlur(img, (5,5), 0)
median = cv.medianBlur(img, 5)
bilateralfilter = cv.bilateralFilter(img,9, 75, 75)
title = ["image", "2D", "blur", 'gaussianblur', 'medianblur', 'bilateralfilter']
image = [img, destination, blur, gaussianblur, median, bilateralfilter]
 
for i in range(6):
    plt.subplot(3,3,i+1),
    plt.imshow(image[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])


plt.show()
