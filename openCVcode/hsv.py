# HUE STATURATION VALUE 
import cv2 as cv
import numpy as np


def func(x):
    pass
cap =cv.VideoCapture(0)

cv.namedWindow("Tracking")
cv.createTrackbar("LH", "Tracking", 0, 255, func)
# this is the trackbar for the lower hue value 
cv.createTrackbar("LS", "Tracking", 0, 255, func)
cv.createTrackbar("LV", "Tracking", 0, 255, func)
cv.createTrackbar("UH", "Tracking", 255, 255, func)
cv.createTrackbar("US", "Tracking", 255, 255, func)
cv.createTrackbar("UV", "Tracking", 255, 255, func)
# L= LOWER, U = UPPER, S = SATURATION, V = VALUE and H = HUE

while(True):
    #frame =cv.imread('lena.jpg')
    _, frame = cap.read()
    # this is reading from your default camera

    hsv= cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # getting the HSV colors
    LH = cv.getTrackbarPos("LH", "Tracking")
    LS = cv.getTrackbarPos("LS", "Tracking")
    LV = cv.getTrackbarPos("LV", "Tracking")

    UH = cv.getTrackbarPos("UH", "Tracking")
    US = cv.getTrackbarPos("US", "Tracking")
    UV = cv.getTrackbarPos("UV", "Tracking")
    lowerblue = np.array([LH, LS, LV])

    #lowerblue = np.array([110,50,50])
    # give us the lower blue color 
    upperblue = np.array([UH, US, UV])
    #upperblue = np.array([130,255,255])
    # Give us the upper blue color
    mask  =cv.inRange(hsv, lowerblue, upperblue)
    # give us the range of the lower and th upper color
    result = cv.bitwise_and(frame, frame, mask=mask)
    # creating a bitwise result of frame with mask value we have created from the upper and lower color

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("result", result)        
    key = cv.waitKey(True)
    if(key==27):
        break
cap.release()
cv.destroyAllWindows()
