import cv2 as cv  
from matplotlib import pyplot as plt    
import numpy as np    



img = cv.imread("../images/lena.jpg")
layer = img.copy()
gaussian_pyr = [layer]
# WE can use pyrUp if wew want to upper the resolution of an image

#lower_resolution_1 = cv.pyrDown(img)
#lower_resolution_2 = cv.pyrDown(lower_resolution_1)
#titles = ['Original', 'lower_resolution_1', 'lower_resolution_2']
#images = [img, lower_resolution_1, lower_resolution_2]
# n = 3
# for i in range(n):
#     x= 3
#     y = 1
#     plt.subplot(x,y, i+1)
#     plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])
# plt.show()
for i in range(3):
    layer = cv.pyrDown(layer)
    gaussian_pyr.append(layer)
    cv.imshow(str(i), layer)
layer = gaussian_pyr[2]
# the laplacian pyramid is like to detect the edges

cv.imshow   ('Upper level of Gaussaian pyramid', layer)
Laplacian_pyr = [layer]
for i in range(2,0,-1):
    gaussian_extend = cv.pyrUp(gaussian_pyr[i])
    laplacian  =cv.subtract(gaussian_pyr[i-1], gaussian_extend)
    cv.imshow(str(i), laplacian)

cv.imshow("Original",img)
#cv.imshow('lower_resolution_1',lower_resolution_1)
#cv.imshow('lower_resolution_2', lower_resolution_2)

cv.waitKey(False)
cv.destroyAllWindows()


