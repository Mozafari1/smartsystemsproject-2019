# Remember, if something is wrong the program will run and it will not give any kind of error
# How do you know when something went worng. check your terminal if you just get the file path and nothing else that means that something went wrong
import cv2

capture =cv2.VideoCapture(0) # using 0 for default camera
# If there is several cameras we need to specify it with  numbers
# Now we using the webcam

fourcc = cv2.VideoWriter_fourcc('X','V','I','D') # you can type *'XVID' 

# This will save the video from the webcame. Here we calling the  'VideoWriter class
# This class will take some arg.
# 1st arg is the name of the output file
# Second arg is four bite codes which is used to specify codecs
# Third arg is the number of frame per sec, the frame typed in form of tuples
save_video = cv2.VideoWriter('../video/webcame.avi', fourcc, 20.0, (640,480))


print(capture.isOpened())
# how to check if you get video from any index ' by index I mean when you give some value instead of '0' in VideoCapture'
# this will give True or False where True means you captureing video


print(["Height Width"])
#while (True):
while(capture.isOpened()):
# making this loop to capture the ret and frame continusly
# You can also use 'capture.isOpened' instead of True in the loop
    ret, frame =capture.read()
    # ret is the boolean variable 
    # This read()  returner true if the frame is available
    if ret == True: 
        width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        #This will give you the height and the width of frame
        a = [height, width]
        print(a)

        save_video.write(frame)# saving the video

        grayColor = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # This give us gray color on the videos

        cv2.imshow("Webcame", grayColor) #frame) # when we want to see gray we need to call the grayColor as second arg in imshow()

        # This will show the frame if the frame is available
    
        if  cv2.waitKey(1) & 0xFF == ord("q"):
        # Here we calling the waitkey() to wait till the user press 'q', then breaking it
            break
    else:
        break

capture.release() 
save_video.release()

cv2.destroyAllWindows()

