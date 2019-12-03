import numpy as np
import cv2

def click_event(event, x,y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # First we read the BGR channels
        # the number shows the number channel
        blue = img[x,y,0]
        green= img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img, (x,y), 3, (0,0,255),-1)
        #this give use a black image 
        imgColor = np.zeros((512, 512,3),np.uint8)
        # This will give use the color of the image when we clicking on that
        # [:] means that we want to fiel every channel on list
        imgColor[:]= [blue, green, red]
        cv2.imshow("color",imgColor)


img = cv2.imread("lena.jpg")
cv2.imshow("Lena",img)
points =[]
cv2.setMouseCallback("Lena", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
