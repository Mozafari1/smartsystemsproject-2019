import os 
from PIL import Image
import cv2 as cv 
import numpy as np     
import pickle 

face_cascade = cv.CascadeClassifier("cascade/data/haarcascade_frontalface_alt2.xml")
recognize = cv.face.LBPHFaceRecognizer_create()

#walking though the directori
base_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(base_dir, "images")

current_id = 0
label_id = {}
y_labels = []
x_train = []

for root, dirs, files, in os.walk(images_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ","-" ).lower()

            #print(label, path)
            if label in label_id:
                pass
            else:
                label_id[label] = current_id
                current_id +=1
            id_ = label_id[label]
            #print(label_id)
            pil_image = Image.open(path).convert("L") # grascale
            new_size = (512,512)
            final_image = pil_image.resize(new_size, Image.ANTIALIAS)

            image_arr = np.array(final_image, "uint8")
            #print(image_arr)

            faces = face_cascade.detectMultiScale(image_arr, 1.2,5)
            for x,y,w,h in faces:
                region_of_interest = image_arr[y:y+h, x:x+w]
                x_train.append(region_of_interest)
                y_labels.append(id_)


#print(y_labels)
#print(x_train)

with open("pickle/labels.pickle", 'wb') as f:
    pickle.dump(label_id, f)
recognize.train(x_train, np.array(y_labels))
recognize.save("yml/trainne.yml")
