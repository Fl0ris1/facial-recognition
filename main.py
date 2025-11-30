import cv2
import os

haar_file="haarcascade_frontalface_default.xml"

datasets="datasets"
subdata="Floris"

#create the directory
path=os.path.join(datasets,subdata)

if not os.path.isdir(path):
    os.makedirs(path)

(width,height)=(130,100)

face_cascade=cv2.CascadeClassifier(haar_file)

webcam=cv2.VideoCapture(0)



