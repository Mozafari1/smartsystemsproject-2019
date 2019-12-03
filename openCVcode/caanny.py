# Canny edge decetor is an edge detection operator that uses a multi-algorithm to detect a wide range of edges in images.
import cv2 as cv 
from matplotlib import pyplot as plt   
# this algorithm can be dertermine as followings steps
# 1 noise reduction, 2 gradient calculation 3, non/maximum suppression, 4 double threshold and finall one is edge tracking by hysteresis

img = cv.imread("../images/butterfly.jpg", 0)
canny = cv.Canny(img, 100, 200)
# Comment use trackbar in canny nad it will ggive better edge with out noises
titels = ['Original','Canny']
images = [img, canny]

n = 2
for i in range(n):
    x = 1
    y = 2
    plt.subplot(x,y,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titels[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
