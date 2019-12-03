import cv2 as cv
#import numpy as np
from matplotlib import pyplot as plt

img= cv.imread('butterfly.jpg',False)
imgc = cv.cvtColor(img, cv.COLOR_BGR2RGB)
_, th1 = cv.threshold(img, 120, 255, cv.THRESH_BINARY)
_, th4 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO)
_, th2 = cv.threshold(img, 120, 255, cv.THRESH_BINARY_INV)
_, th5 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO_INV)
_, th3 = cv.threshold(img, 200, 255, cv.THRESH_TRUNC)
titles = ['Orginal picture','THRESH_BINARY', 'THRESH_TOZERO','THRESH_TRUNC' ,'THRESH_BINARY_INV  ','  THRESH_TOZERO_INV']
images = [img,th1, th4, th3,th4,th5]

for i in range(6):
    plt.subplot(3,3,i+1),
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),
    plt.yticks([])
# cv.imshow("Image", img)
# cv.imshow("th1", th1)
# cv.imshow("th2", th2)
# cv.imshow("th3", th3)
# cv.waitKey(False)
# cv.destroyAllWindows()

plt.show()
