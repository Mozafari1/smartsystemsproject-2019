import cv2 as cv 
import numpy as np     
import pickle 

recognize = cv.face.LBPHFaceRecognizer_create()
face_cascade = cv.CascadeClassifier("cascade/data/haarcascade_frontalface_alt2.xml")
eyes_cascade = cv.CascadeClassifier("cascade/data/haarcascade_eye.xml")
recognize.read("yml/trainne.yml")

lables = {"name":1}
with open("pickle/labels.pickle", 'rb') as f:
    original_labels = pickle.load(f)
    labels  ={value:key for key,value in original_labels.items()}
cap = cv.VideoCapture(False)
while cap.isOpened():
    # capture frame by frame
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    #face
    faces = face_cascade.detectMultiScale(gray, 1.05,5)
    print(faces);
    for x,y,w,h in faces:
        print(x,y,w,h)
        region_of_interest_gray  = gray[y:y+h, x:x+w]
        region_of_interest_color = img[y:y+h, x:x+w]
        #recognize 
        id_, confidence = recognize.predict(region_of_interest_gray)
        if confidence >= 50 and confidence<130:

            print(id_)
            print(labels[id_])
            cv.putText(img, labels[id_], (x,y), cv.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2, cv.LINE_AA)
        img_item  ="picture/image.png"
        cv.imwrite(img_item, region_of_interest_gray)
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
        #eyes
        eyes = eyes_cascade.detectMultiScale(region_of_interest_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(region_of_interest_color, (ex,ey), (ex+ew, ey+eh), (0,255,0),2)
    # display img 
    cv.imshow("Camera", img)
    if  cv.waitKey(20) & 0xFF ==ord ('q'):
        break

# done then relase
cap.release()
cv.destroyAllWindows()


