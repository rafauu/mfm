import cv2
import numpy as np
import os 
import requests
from time import sleep

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

names = ['Rafau1', 'Rafau2']

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    if len(faces):
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, _ = recognizer.predict(gray[y:y+h,x:x+w])
            cv2.putText(img, names[id], (x+5,y-5), font, 1, (255,255,255), 2)
            requests.post('http://localhost:5000/process', json={'name':names[id]})
    else:
        requests.post('http://localhost:5000/process', json={'name':''})

    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()
