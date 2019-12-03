import cv2 as cv  
import numpy as np    
import pickle 

recognize = cv.face.LBPHFaceRecognizer_create()
fb = cv.CascadeClassifier("cascade/data/haarcascade_fullbody.xml")
ub = cv.CascadeClassifier("cascade/data/haarcascade_upperbody.xml")
lb = cv.CascadeClassifier("cascade/data/haarcascade_lowerbody.xml")

face_cascade = cv.CascadeClassifier("cascade/data/haarcascade_profileface.xml")
eyes_cascade = cv.CascadeClassifier("cascade/data/haarcascade_eye.xml")
recognize.read("yml/trainne.yml")

lables = {"name":1}
with open("pickle/labels.pickle", 'rb') as f:
    original_labels = pickle.load(f)
    labels  ={value:key for key,value in original_labels.items()}
#cap = cv.VideoCapture(False)

while True:
    ret, img = cap.read()
    if ret == True:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        fbody = fb.detectMultiScale(gray, 1.1, 4)

        for  (x,y,h,w) in fbody:
            print(x,y,w,h)
            region_of_interest_gray  = gray[y:y+h, x:x+w]
            region_of_interest_color = img[y:y+h, x:x+w]
            cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
            # Upper body
        ubody = ub.detectMultiScale(gray, 1.1, 4)
        for xu, yu, hu, wu in ubody:
            region_of_interest_gray  = gray[yu:yu+hu, xu:xu+wu]
            region_of_interest_color = img[yu:yu+hu, xu:xu+wu]
            cv.rectangle(region_of_interest_color, (xu, yu), (xu+wu, yu+hu), (0,255,0), 2)
                # recognize
            faces = face_cascade.detectMultiScale(region_of_interest_gray)    
            for fx, fy, fw, fh in faces:
                id_, confidence = recognize.predict(region_of_interest_gray)
                if confidence >= 50 and confidence<130:
                    print(id_)
                    print(labels[id_])
                    cv.putText(img, labels[id_], (fx,fy), cv.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2, cv.LINE_AA)
                img_item  ="picture/image.png"
                cv.imwrite(img_item, region_of_interest_gray)
                cv.rectangle(img, (fx,fy), (fx+fw, fy+fh), (0,255,0),2)

                eyes = eyes_cascade.detectMultiScale(region_of_interest_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv.rectangle(region_of_interest_color, (ex,ey), (ex+ew, ey+eh), (0,255,0),2)
            # Lower body
        lbody = lb.detectMultiScale(region_of_interest_gray)
        for lx, lw, lh, ly in lbody:
            cv.rectangle(region_of_interest_color, (lx, ly), (lx+lw, ly+lh), (0,255,0), 2)
  

        cv.imshow('Camera', img)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
