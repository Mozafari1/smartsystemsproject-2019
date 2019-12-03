import numpy as np
import cv2

#image = cv2.imread("lena.jpg",1)
image = np.zeros([512,512, 3],np.uint8) # this will give use black image

# with cv2.line() we can draw lines. this will take some arg
# The coordinate is given in tuples, The color is given BGR 
# 1st is image, second is start coordinate, the third is end coordinate
# 4th is color and 5th is thickness
image = cv2.line(image,(0,0),(255,255),(255,0,0),1) # overwriting  image first
image = cv2.arrowedLine(image, (255,0),(0,0),(23,234,0),1)

image = cv2.rectangle(image, (0,300),(500,200),(234,0,8),1)
image = cv2.circle(image, (445,34), 34,(0,76,34),3)
image = cv2.putText(image, 'Lenas', (4,110), cv2.FONT_HERSHEY_COMPLEX, 5, (234,70,80),8, cv2.LINE_AA)


cv2.imshow("Lena's Photo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
