import numpy as np
import cv2

# this will print out all the events in cv2 package
# We are using a condition and if 'EVENT' is in that properties we printing out 
# events = [i for i in dir(cv2) if 'EVENT' in i] 
# print(events)

#We are writing a program for mouse. When we are clicking its goring to do something

# this is a callback function, takes few arg, 1st is mouse_event, x&y is coordinate, 4th is flags and 5th is param
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: # If the left mouse button is clicked print x and y coordonate
        
        print("Coordinate")
        print("  y",'  '," x ")
        print("------------")
        print('[',x, ' ', y,']')
        print()
        font= cv2.FONT_HERSHEY_COMPLEX
        xy = str(x) +', '+ str(y) 
        cv2.putText(img, xy, (x,y),font, 1, (255,0,0),1)
        cv2.imshow("Webcam", img)

    if event== cv2.EVENT_RBUTTONDOWN:# if u click on right 
        blue= img[y,x, 0]
        green= img[y,x, 1]
        red= img[y,x, 2]
        bgr = str(blue)+ ', '+ str(green)+', '+str(red)
        cv2.putText(img, bgr, (x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,34),1)
        cv2.imshow("Webcam",img)
        print("Colors")
        print("  blue ","green ","red")
        print("---- ---- ---- ----")
        print('[',blue, '  ', green,'  ',red, ']')
        print()
#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread("lena.jpg")
cv2.imshow("Webcam", img)
cv2.setMouseCallback("Webcam",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
