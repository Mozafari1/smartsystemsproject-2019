import numpy as np
import cv2

img = cv2.imread("../images/lena.jpg")
img1 = cv2.imread('../images/me.jpg')

print(img.shape) 
# this will returns a tuple of number o rows, colum ...
print(img.size)
# this will returns total number of pixels is accessed
print(img.dtype)
# this will returns image datatype is obtained
b,g,r = cv2.split(img)
# this spliting the image in blue, green and red colors
img = cv2.merge((b,g,r))
# Merging the image and give use a whole  image not splitted
img = cv2.resize(img, (512,400))
img1 = cv2.resize(img1, (512, 400))
# Here I reszising the images if they have different size and it will give use some error


#new_img = cv2.add(img, img1)# adding both image in one, they cover over the other 
new_img = cv2.addWeighted(img, .8, img1, .2,0) # this will help use with how much percent of the first and the second image we will take 
# taking few arg. 1st is image 1, 2th is percent (you can also type in 0-1), 3th is second image and last one is percent of the second image

cv2.imshow("Image", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
