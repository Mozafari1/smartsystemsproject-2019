import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread("apple.jpg", -1)

cv.imshow('Image', img)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img)
#plt.xticks([]), plt.yticks([])

plt.show()

cv.waitKey(False)
cv.destroyAllWindows()
