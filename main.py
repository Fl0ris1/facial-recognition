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

for i in range(1,31):
    status,frame=webcam.read()

    if not status:
        print("Unable to access webcam")
        break

    grayscale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(grayscale,1.3,4)

    #check if the faces are detected
    if len(faces)>0:
        for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            face=grayscale[y:y+h,x:x+w]
            facial_resize=cv2.resize(face,(width,height))
            cv2.imwrite(os.path.join(path,f"{i}.png"),facial_resize)

    cv2.imshow("faces",frame)

    key=cv2.waitKey(300)
    if key==27:
        break
    
webcam.release()
cv2.destroyAllWindows()