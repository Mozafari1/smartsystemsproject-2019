import cv2
import numpy as np

img1 = np.zeros((300,500,3), np.uint8)
img1 = cv2.rectangle(img1, (200,0), (300,100),(255,255,255),-1)
# This will creating a white rectangle inside the black image we getting from the np.zeros
# Demnesjoner og colors
img2 = cv2.imread("../images/lena.jpg")

# The image must be resized to get performed bitwise
img2 = cv2.resize(img2, (500,300)) 
bitand = cv2.bitwise_and(img2,img1)
# Performing bitwise operations for both images
# Here I do some logic operation which is and operation, Look at truth table for and gate  when A and B is high we get the output high
bit_or = cv2.bitwise_or(img2,img1)
# # or operation
# bit_not = cv2.bitwise_not(img2, img1)
# # nor operation
bit_xor = cv2.bitwise_xor(img1,img2)
#xor operation

cv2.imshow("image1", img1)
cv2.imshow("Lena",img2)
cv2.imshow("bitand", bitand)
cv2.imshow("bitor", bit_or)
# cv2.imshow("bitnot", bit_not)
cv2.imshow("bitxor", bit_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()
