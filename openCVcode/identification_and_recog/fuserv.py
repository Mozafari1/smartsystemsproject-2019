import pickle 
import cv2 as cv  
import numpy as np    
import RPi.GPIO as GPIO
import time
ub = cv.CascadeClassifier("cascade/data/haarcascade_upperbody.xml")
face_cascade = cv.CascadeClassifier("cascade/data/haarcascade_frontalface_alt2.xml")
cap = cv.VideoCapture(False)
#cap = cv.VideoCapture("images/fb/mkv/vtest.avi")
recognize = cv.face.LBPHFaceRecognizer_create()
recognize.read("yml/trainne.yml")
lables = {"name":1}
def func (): 
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
            # Motion Detection
            _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
            dilated = cv.dilate(thresh, None, iterations=4)
            contours, _ = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_TC89_KCOS)
            for contour in contours:
                (x, y, w, h)  =cv.boundingRect(contour)
                if cv.contourArea(contour)<2000:
                    continue
                else:
                    cv.rectangle(frame0, (x,y), (x+w, y+h), (0,255,0),2)
                    cv.putText(frame0, "Movement", (x,y), cv.FONT_ITALIC, 1, (0,255,255),1)
                    print("Movement coordinates: ", '{',x,y,h,w,'}')

            # Upbber body detection
            ubody = ub.detectMultiScale(median, 1.2,4)
            for xu, yu, hu, wu in ubody:
                cv.putText(frame0,"Upperbody",  (xu,yu), cv.FONT_ITALIC, 1,(0,255,255), 1, cv.LINE_AA)
                cv.rectangle(frame0, (xu, yu), (xu+wu, yu+hu), (0,150,255), 2)
                print("UpperBody coordinates: ", '{',xu, yu, hu, wu,'}')
            # Face cascade
            faces = face_cascade.detectMultiScale(median, 1.3,5)    
            for fx, fy, fw, fh in faces:
                print("Face coordinates: ",'{',fx,fy,fh,fw,'}')
                region_of_interest_gray  = median[fy:fy+fh, fx:fx+fw]
                id_, confidence = recognize.predict(region_of_interest_gray)
                if confidence >= 50 and confidence<130:
                    print("Id: ", id_)
                    print("Name: ", labels[id_])
                    cv.putText(frame0, labels[id_], (fx,fy), cv.FONT_ITALIC, 1,(0,255,255), 1, cv.LINE_AA)
                img_item  ="picture/image.pnsg"
                cv.imwrite(img_item, region_of_interest_gray)
                cv.rectangle(frame0, (fx,fy), (fx+fw, fy+fh), (16,0,200),2)
                if (id_!=id_):
                    
    # Targer area
                    nfw = int(fw/2)
                    nfh = int(fh/2)
                    cv.rectangle(frame0, (fx,fy), (fx+nfw, fy+nfh), (200,0,200),2)
                    cv.line(frame0, (fx+nfw,fy), (fx+nfw, fy+nfh), (200,0,200),2)

                    print("New_1 Face coordinates: ",'{',fx,fy,nfh,nfw,'}')
                    
                    nfx = int(fx+nfw)
                    nfy = int(fy+nfh)
                    cv.rectangle(frame0, (nfx,nfy), (nfx+nfw, nfy+nfh), (200,0,200),2)
                    print("New_2 Face coordinates: ",'{',nfx,nfy,nfh,nfw,'}')
                    cv.rectangle(frame0, (nfx,fy), (nfx+nfw, fy+nfh), (200,0,200),2)
                    cv.rectangle(frame0, (fx,nfy), (fx+nfw, nfy+nfh), (200,0,200),2)
                    cv.line(frame0, (fx+nfw,fy), (fx+nfw, nfy+nfh), (200,0,200),2)          # Y akse

                    cv.line(frame0, (fx,nfy), (nfx+nfw, fy+nfh), (200,0,200),2)          # X akse
                    cv.line(frame0, (fx+nfw, nfy+nfh), (nfx+nfw, fy+nfh+nfh), (200,0,200),2)          # X akse

                    cv.circle(frame0,(nfx,nfy),int(nfh/2),(33,100,99),2)
                    print("New_Y Face coordinates: ",'{',fx+nfw,fy, fx+nfw, nfy+nfh,'}')
                    print("New_X Face coordinates: ",'{',fx,nfy, nfx+nfw, fy+nfh,'}')

                    print("Circle: ",nfx,nfy, int(nfh/2))
                    

                    

                    cv.line(frame0, (fx+nfw, nfy+nfh), (fx+nfw, fy+fh*2), (16,0,200),2)
                    print("Target coordinates: ",'{',fx+nfw, nfy+nfh, fx+nfw, fy+fh*2,'}')
                    #---------------------------------------------------------------------------------------- Target
                    #The Target circle
                    
                    cX_fx_nfw  = fx+nfw
                    cY_fy_fh_2 = fy+fh*2
                    radius = int(nfh/2)
                    cv.circle(frame0,(cX_fx_nfw, cY_fy_fh_2),radius,(0,255,0),2)
                    cv.putText(frame0, "Target aim", (cX_fx_nfw,cY_fy_fh_2), cv.FONT_ITALIC, 1, (0,255,255),1)
                    print("C_Target Coord: ",'{',cX_fx_nfw,cY_fy_fh_2,radius,'}')
                    new_nfw = int(nfw/2)
                    # The x axis
                    X_slX = cX_fx_nfw-new_nfw
                    X_slY = cY_fy_fh_2
                    X_elX = nfx+new_nfw
                    X_elY = nfy+nfh*3
                    cv.line(frame0, (X_slX,X_slY), (X_elX,X_elY), (0,0,255),2)
                    print("_Target_X_Coord: ",'{',X_slX,X_slY, X_elX,X_elY,'}')
                    # The y axis
                    new_nfh = int(nfh/2)
                    Y_slX = cX_fx_nfw
                    Y_slY = cY_fy_fh_2
                    Y_elX = cX_fx_nfw 
                    Y_elY = X_elY + new_nfh
                    
                    cv.line(frame0, (Y_slX,Y_slY), (Y_elX, Y_elY), (0,0,255),2) 
                    print("_Target_Y_Coord: ",'{',Y_slX,Y_slY, Y_elX,Y_elY,'}')
                    # The inner Circle
                    new_radius = int(radius/5)
                    cv.circle(frame0,(Y_slX,Y_slY-new_radius),new_radius,(0,200,255),2)
                    print("_Target_InnerC_Coord: ",'{',Y_slX,Y_slY-new_radius, new_radius,'}')
                    
                #   ------------------ The y axis for aim targeting
                #   First we start to move the x axis from the (x,y) coordinate
                #   Then running the y axis out from the length of radius 
                #   This is our best change to get achive the target we want to aim and fire by laser

    #------------------------------------------ Sevo
                    externarray = [fx,fy,fh,fw]
                    def fireaim(externarray):
                        stop = False
                        a = np.zeros(4)
                        np.put(a, [0,1,2,3], externarray)
                        servox = 22
                        servoy = 11
                        sirled = 8

                        gpio.setmode(gpio.BOARD)
                        gpio.setup(servox, gpio.OUT)
                        gpio.setup(servoy, gpio.OUT)
                        gpio.setup(sirled, gpio.OUT)

                        sirx = gpio.PWM(servox, 50)
                        siry = gpio.PWM(servoy, 50)

                        sirx.start(0)
                        siry.start(0)

                        angle = 0
                        #dutycycle = ((angle/180.0)+1.0)*5

                        try:
                            while not stop:
                                centerx = (a[2]-a[0])/2
                                centery = (a[3]-a[1])/2
                                siktx = ((centerx/90.0)+1.0)*5
                                sirx.ChangeDutyCycle(siktx)
                                time.sleep(.2)
                                gpio.output(sirled, gpio.LOW)

                                sikty = ((centery/90.0)+1.0)*5
                                siry.ChangeDutyCycle(sikty)
                                time.sleep(.5)
                                gpio.output(sirled, gpio.HIGH)
                                stop = True

                        except KeyboardInterrupt:
                            sirx.stop()
                            siry.stop()
                            gpio.cleanup()

                    fireaim(externarray)
   
                # #--------------------------------------------

                else:
                    pass



            cv.imshow("Pi Camera NoIR", frame0)
            frame0 = frame1 
            ret, frame1  = cap.read()
            if(cv.waitKey(40)==27):
                break
        else:
            break
    cv.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    func()




