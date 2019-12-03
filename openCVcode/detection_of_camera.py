import cv2 as cv  
import numpy as  np 
capture= cv.VideoCapture(False)
#capture = cv.VideoCapture('../images/vtest.avi')
fourcc = cv.VideoWriter_fourcc('X','V','I','D') # you can type *'XVID' 
save_video = cv.VideoWriter('CAMERA.avi', fourcc, 20.0, (640,480))
print(capture.isOpened())
ret, frame0 = capture.read()
ret, frame1 = capture.read()

while capture.isOpened():
    difference = cv.absdiff(frame0, frame1)
    gray  = cv.cvtColor(difference, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5),0)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (x, y, w, h)  =cv.boundingRect(contour)
        if cv.contourArea(contour)<1200:
            continue
        else:
            cv.rectangle(frame0, (x,y), (x+w, y+h), (0,255,0),2)
            cv.putText(frame0, "Status: {}".format('Movment'), (10,20), cv.FONT_HERSHEY_SIMPLEX, 1, (200,0,170),2)
    #cv.drawContours(frame0, contours, -1, (0,255,0),2)

    cv.imshow("CAMERA", frame0)
    frame0 = frame1 
    ret, frame1  = capture.read()


    if(cv.waitKey(40)==27):
        break

cv.destroyAllWindows()
capture.release()
save_video.release()



