import cv2 as cv
import numpy as np
def nothing (x): # it is callback function with the value of current postion
    print(x)

img = np.zeros((300, 512,3), np.uint8)
cv.namedWindow('image') #Creating a window with a name image

cv.createTrackbar('B','image',0, 255, nothing)
cv.createTrackbar('G','image',0, 255, nothing)
cv.createTrackbar('R','image',0, 255, nothing)
# In the image window we are going to add B trackbar 
# B is the trackbar name, image, value wich is the initial value the is set and next is the final value u want to set and last is callback function
# the callback function is called when the trackbar is chaning

switch = '0 : False\n 1 : True'
cv.createTrackbar(switch, 'image',False,True, nothing)
# this is a switch trackbar 
while(True): # This loop show the image and when we press the ESC button it will collaps
    cv.imshow("image", img)
    i = cv.waitKey(True) & 0xFF
    if i ==27:
        break
    # creating variable to get the trackbr valuesand use it in image
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r  = cv.getTrackbarPos('R', 'image')
    s  = cv.getTrackbarPos(switch,'image')
    if s== 0: # this condition is going to be true when the s is not 0 
        img[:] = 0 
    else:
    # now we putting this values in an empty arry
        img [:] = [b, g, r]

cv.destroyAllWindows()
