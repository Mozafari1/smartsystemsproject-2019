import cv2 as cv
import numpy as np  
from matplotlib import pyplot as plt    
img = cv.imread("../images/butterfly.jpg", cv.IMREAD_GRAYSCALE)

# declaring/ clearing/firmly a variable  and calling the function twhich are available inside the opencv lib
# this function will take few arguments which are the following: img, datatype, 64F is 64 bits flots
# using this 64F due to he negative slope induced by transforming th eimage from withe to black 

laplas = cv.Laplacian(img, cv.CV_64F, ksize=1)
#Taking the absolute value of laplacian image and converting this value into unsigned 8 bits integer for our outputs
laplas = np.uint8(np.absolute(laplas))
#The sobel gradient image take 4 argu and the 3rd value is 1 and it means that we using for X and 0 in this case for Y 
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0) # 1 for X direction and 0 for y direction
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)

# now we need to convert this values into unsigned 8 bits integer
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
combineX_Y_OR = cv.bitwise_or(sobelX, sobelY)
combineX_Y_XOR = cv.bitwise_xor(sobelX, sobelY)
combineX_Y_AND = cv.bitwise_and(sobelX, sobelY)
combineX_Y_NOT  =cv.bitwise_not(sobelX, sobelY)

titles = ['Original','Laplacian', 'SobelX', 'SobelY','combineX_Y_OR','combineX_Y_XOR','combineX_Y_AND','combineX_Y_NOT']
images = [img, laplas, sobelX, sobelY,combineX_Y_OR,combineX_Y_XOR,combineX_Y_AND,combineX_Y_NOT]

for i in range(8):
    plt.subplot(3,3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
