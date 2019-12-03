import cv2 as cv 
import numpy as np
from matplotlib import pyplot as plt 

apple  = cv.imread("../images/apple.jpg")
orange = cv.imread ("../images/orange.jpg")
print(apple.shape)
print(orange.shape)

half_A_O = np.hstack((apple[:, :256], orange[:, 256:]))
#Generate Gaussian pyramid for apple
apple_copy = apple.copy()
apple_gp = [apple_copy]

for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    apple_gp.append(apple_copy)


#Generate Gaussaian pyramid for origange
orange_copy = orange.copy()
orange_gp = [orange_copy]

for i in range(6):
    orange_copy = cv.pyrDown(orange_copy)
    orange_gp.append(orange_copy)

# Generate Laplacian pyramiid for appel and orange

apple_copy = apple_gp[5]
laplacian_apple = [apple_copy]
for i in range (5, 0,-1):
    gaussaian_extend = cv.pyrUp(apple_gp[i])
    laplacian = cv.subtract(apple_gp[i-1], gaussaian_extend)

    laplacian_apple.append(laplacian)


orange_copy = orange_gp[5]
laplacian_orange = [orange_copy]
for i in range (5, 0,-1):
    gaussaian_extend = cv.pyrUp(orange_gp[i])
    laplacian = cv.subtract(orange_gp[i-1], gaussaian_extend)

    laplacian_orange.append(laplacian)

# Adding left and right halvs of images in each level

apple_orange_pyr = []
n = 0
for apple_laplacian, orange_laplacian in zip(laplacian_apple, laplacian_orange):
    n +=1
    cols, rows, ch = apple_laplacian.shape  
    laplacian  = np.hstack((apple_laplacian[:, 0:int(cols/2)], orange_laplacian[:, int(cols/2):]))
    apple_orange_pyr.append(laplacian)


# now its time to reconstruct our images
apple_orange_recons = apple_orange_pyr[0]
for i in range(1,6):
    apple_orange_recons =cv.pyrUp(apple_orange_recons)
    apple_orange_recons = cv.add(apple_orange_pyr[i],apple_orange_recons)

cv.imshow("Apple", apple)
cv.imshow("Orange", orange)
cv.imshow("Half_A_O", half_A_O)
cv.imshow('apple_orange_recons', apple_orange_recons)
cv.waitKey(False)
cv.destroyAllWindows()
