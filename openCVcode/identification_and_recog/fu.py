import pickle 
import cv2 as cv  
import numpy as np    

ub = cv.CascadeClassifier("cascade/data/haarcascade_upperbody.xml")
face_cascade = cv.CascadeClassifier("cascade/data/haarcascade_frontalface_alt2.xml")
cap = cv.VideoCapture(False)

#cap = cv.VideoCapture("images/fb/mkv/vtest.avi")
recognize = cv.face.LBPHFaceRecognizer_create()
recognize.read("yml/trainne.yml")

lables = {"name":1}
with open("pickle/labels.pickle", 'rb') as f:
    original_labels = pickle.load(f)
    labels  ={value:key for key,value in original_labels.items()}

while cap.isOpened():
    ret, frame0 = cap.read()
    ret, frame1 = cap.read()
    if ret == True:
        difference = cv.absdiff(frame0, frame1)
        gray  = cv.cvtColor(difference, cv.COLOR_BGR2GRAY)
        gr = cv.cvtColor(frame0, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (5,5),0)
        median = cv.medianBlur(gr, 3)
        # New filtring method
        laplas = cv.Laplacian(median, cv.CV_64F, ksize=1) # creating a laplacian img this will separate the img from its background
        laplas = np.uint8(np.absolute(laplas))
        thresh_gaussian = cv.adaptiveThreshold(median, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,15, 2)


        # we filtring the image and getting better result
        _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
        dilated = cv.dilate(thresh, None, iterations=3)
        contours, _ = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_TC89_KCOS)
        for contour in contours:
            (x, y, w, h)  =cv.boundingRect(contour)
            if cv.contourArea(contour)<1500:
                continue
            else:

                cv.rectangle(frame0, (x,y), (x+w, y+h), (0,255,0),2)
                cv.putText(frame0, "Status: {}".format('Movment'), (x,y), cv.FONT_ITALIC, 1, (0,255,255),1)
                print("Movement coordinates: ", '{',x,y,h,w,'}')

        ubody = ub.detectMultiScale(thresh_gaussian, 1.06,4)
        for xu, yu, hu, wu in ubody:
            cv.putText(frame0,"Upperbody",  (xu,yu), cv.FONT_ITALIC, 1,(0,255,255), 1, cv.LINE_AA)
            cv.rectangle(frame0, (xu, yu), (xu+wu, yu+hu), (0,150,255), 2)
            print("UpperBody coordinates: ", '{',xu, yu, hu, wu,'}')

        faces = face_cascade.detectMultiScale(median, 1.2,5)    
        for fx, fy, fw, fh in faces:
            print("Face coordinates: ",'{',fx,fy,fh,fw,'}')
            
            region_of_interest_gray  = median[fy:fy+fh, fx:fx+fw]
            id_, confidence = recognize.predict(region_of_interest_gray)
            if confidence >= 50 and confidence<130:
                print("id: ", id_)
                print("Name: ", labels[id_])
                cv.putText(frame0,labels[id_], (fx,fy), cv.FONT_ITALIC, 1,(0,255,255), 1, cv.LINE_AA)

            img_item  ="picture/image.png"
            cv.imwrite(img_item, region_of_interest_gray)
            cv.rectangle(frame0, (fx,fy), (fx+fw, fy+fh), (16,0,200),2)

        cv.imshow("Camera", frame0)
        frame0 = frame1 
        ret, frame1  = cap.read()


        if(cv.waitKey(40)==27):
            break
    else:
        break

cv.destroyAllWindows()
cap.release()