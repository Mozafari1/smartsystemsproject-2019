# This program will help to detect object. written in python and easy to use.  Read The README file before you wanna use this. 
import numpy as np   
import cv2 as cv 
from matplotlib import pyplot as plt       

capture_video = cv.VideoCapture(False)
write_video_fourcc = cv.VideoWriter_fourcc("X","V","I", "D")
save_video = cv.VideoWriter("../video/MDVR.avi",write_video_fourcc, 20.0, (512, 512))
#Print out if the VC is opened otherwise give error

print(capture_video.isOpened())

while(True):
    ret, frame0 = capture_video.read()
    ret, frame1 = capture_video.read()
    difference = cv.absdiff(frame0,frame1)
    gray = cv.cvtColor(difference, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray,(5,5),0)
    _, threshold = cv.threshold(blur, 20,255, cv.THRESH_BINARY)
    dilated = cv.dilate(threshold, None, iterations=3)
    contours, _ = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (x_axis, y_axis, width, height) = cv.boundingRect(contour)
        if(cv.contourArea(contour)<900):
            continue
        else:
            cv.rectangle(frame0, (x_axis, y_axis), (x_axis+width, y_axis+height), (0,255,0),2)
            cv.putText(frame0, "Status: {}".format("Movement"),(10,20), cv.FONT_HERSHEY_SIMPLEX, 1, (200,0,170),2)


    #ret, frame = capture_video.read()
    if ret ==True:
        
        width = capture_video.get(cv.CAP_PROP_FRAME_WIDTH)
        height = capture_video.get(cv.CAP_PROP_FRAME_HEIGHT)
        x_and_y = [width, height]
        print(x_and_y)
        
        
        cv.imshow("MDVR_Camera", cv.cvtColor(frame0, cv.COLOR_BGR2GRAY))
        frame0 = frame1
        ret, frame1 = capture_video.read()
        save_video.write(frame0)
        if(cv.waitKey(True) & 0xFF ==ord('q')):
            break
    else:
        print("Something went wrong, please check the error!")
        break;
capture_video.release()
save_video.release()
cv.destroyAllWindows()





