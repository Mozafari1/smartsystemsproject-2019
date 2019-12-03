import numpy as np   
import cv2 as cv  

from matplotlib import pylab as plt       
# img = np.zeros((300,300), np.uint8)
# cv.rectangle(img,(0,100),(200,200),(255),-1)
# cv.rectangle(img, (0,50), (100,300),(150),-1)
img = cv.imread("../images/bikini.jpg")

b,g,r = cv.split(img)

# cv.imshow("img", img)
# cv.imshow("b",b)
# cv.imshow("g", g)
# cv.imshow("r", r)
plt.hist(img.ravel(),256,[0,256] )
plt.hist(b.ravel(),256,[0,256] )
plt.hist(g.ravel(),256,[0,256] )
plt.hist(r.ravel(),256,[0,256] )
#hist = cv.calcHist([img], [0], None, [256], [0,256])
#plt.plot(hist)
plt.show()

cv.waitKey(False)
cv.destroyAllWindows()

