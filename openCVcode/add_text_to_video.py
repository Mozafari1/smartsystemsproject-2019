import cv2
import datetime

capture = cv2.VideoCapture(0)

print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
#capture.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
# capture.set(3,700)
# capture.set(4,700)

# print(capture.get(3))
# print(capture.get(4))

while (True):
    ret, frame = capture.read()
    if ret==True:
        cv2.line(frame, (0,0),(200,400),(255,0,23),2)
        cv2.arrowedLine(frame,(450,0),(340,555),(0,0,255),1)
        cv2.rectangle(frame,(0,340),(330,200),(0,255,0),2)
        cv2.circle(frame,(234,453),50,(34,0,45),2)
        cv2.putText(frame,"Webcam", (0,200), cv2.FONT_HERSHEY_COMPLEX,4,(255,0,0),6, cv2.LINE_AA)

        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text_h_w = "Width: "+str(capture.get(3)) + "Height: "+str(capture.get(4))
        date = "Webcam " + str(datetime.datetime.now())
        frame = cv2.putText(frame, date, (190,40),font,1,(255,0,0),1,cv2.LINE_AA)
        
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow ('Lenas photo', frame)

        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
