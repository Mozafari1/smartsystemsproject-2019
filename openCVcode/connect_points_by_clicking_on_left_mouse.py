import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y),3,(0,0,255),-1)
        # We drawing circles on image and then drawing again then connecting them by line
        points.append((x,y))
        # We calling the array and saving the coordinate when each time the mouse is clicked
        if len(points)>= 2:
            # Here if the length of points is => 2 then connecting them by a line
            cv2.line(img, points[-1], points[-2], (0,200,0),1)
            # We connecting the last and the second last element on the array
            
        cv2.imshow("Picture", img)


img = np.zeros((512, 512,3), np.uint8)
#img= cv2.imread("lena.jpg")
cv2.imshow("Picture", img)
points = []
# this is an empty array where we use it for coordiante
cv2.setMouseCallback("Picture",click_event )
cv2.waitKey(0)
cv2.destroyAllWindows()
