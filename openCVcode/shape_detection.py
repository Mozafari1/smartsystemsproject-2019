import numpy as np    
import cv2 as cv   
img  = cv.imread("../images/shapes.jpg")
imggray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(imggray, 240, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for c in contours:
    approx = cv.approxPolyDP(c, 0.01*cv.arcLength(c, True), True)
    cv.drawContours(img, [approx], 0, (0,0,0), 3)
    x_cor = approx.ravel()[0]
    y_cor = approx.ravel()[1] -6
    if(len(approx)==3):
        cv.putText(img, "Triangle", (x_cor, y_cor), cv.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0))
    elif (len(approx)==4): 
        xx, yy, w, h  = cv.boundingRect(approx)
        aspectRatio  = float(w)/h 
        print(aspectRatio) 
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:

            cv.putText(img, "Square", (x_cor, y_cor), cv.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0))
        else:
            cv.putText(img, "Rectangle", (x_cor, y_cor), cv.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0))
 
    elif(len(approx)==5):
        cv.putText(img, "Pentagon", (x_cor, y_cor), cv.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0))
    elif(len(approx)==10):
        cv.putText(img, "Star", (x_cor, y_cor), cv.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0))
    else:
        cv.putText(img, "Cirle", (x_cor, y_cor), cv.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0))

cv.imshow("Shapes Ori", img)
cv.waitKey(False)
cv.destroyAllWindows()
