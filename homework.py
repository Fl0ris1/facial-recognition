import cv2
import os

haar_cascade="haarcascade_frontalface_default.xml"

datasets="datasets"

subdata="Family"

path=os.path.join(datasets,subdata)

if not os.path.isdir(path):
    os.makedirs(path)

width,height=(150,150)

facecascade=cv2.CascadeClassifier(haar_cascade)

webcam=cv2.VideoCapture(0)

for i in range(30):
    status,frame=webcam.read()
    if not status:
        print("error")
        break

    grayscale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=facecascade.detectMultiScale(grayscale,1.3,4)


    
webcam.release()
cv2.destroyAllWindows()