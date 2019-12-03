import cv2 as cv
import numpy as np
def nothing (x): # it is callback function with the value of current postion
    print(x)

cv.namedWindow('image') #Creating a window with a name image

cv.createTrackbar('CP','image',0, 255, nothing)

# In the image window we are going to add B trackbar 
# B is the trackbar name, image, value wich is the initial value the is set and next is the final value u want to set and last is callback function
# the callback function is called when the trackbar is chaning

switch = 'color/gray'
cv.createTrackbar(switch, 'image',False,True, nothing)
# this is a switch trackbar 
while(True): # This loop show the image and when we press the ESC button it will collaps
    img = cv.imread('../images/lena.jpg')
    current_pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_COMPLEX_SMALL
    cv.putText(img, str(current_pos), (40,130),font, 3, (0,255,0))

    i = cv.waitKey(True) & 0xFF
    if i ==27:
        break
    # creating variable to get the trackbr valuesand use it in image
 
    s  = cv.getTrackbarPos(switch,'image')
    if s== 0: # this condition is going to be true when the s is not 0 
        pass
    else:
    # now we putting this values in an empty arry
        img =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img = cv.imshow("image", img)
cv.destroyAllWindows()
