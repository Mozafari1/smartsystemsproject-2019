import cv2 as cv  
import numpy as  np 

#capture = cv.VideoCapture('../images/vtest.avi')
capture = cv.VideoCapture(False)
face_cascade = cv.CascadeClassifier("../xml/face_default.xml") # face


while capture.isOpened():
    ret, frame0 = capture.read()

    gray  = cv.cvtColor(frame0, cv.COLOR_BGR2GRAY)
    face =face_cascade.detectMultiScale(gray, 1.3,5)
    for x,y, w, h in face:
        cv.rectangle(frame0, (x,y), (x+w, y+h), (0,255,0),2)
        g = gray[y:y+h, x:x+w]
        color = frame0[y:y+h, x:x+w]

    cv.imshow("Face Cascading", frame0)
    if(cv.waitKey(40)==27):
        break

capture.release()

cv.destroyAllWindows()


