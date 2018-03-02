import cv2
import numpy as np

#recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer = cv2.face.LBPHFaceRecognizer_create()

FaceDetect = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
recognizer.read("recognizer\\trainingData.yml")
#font =cv2.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX,4,1,0,4)
id=0
while 1:
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    faces = FaceDetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=recognizer.predict(gray[y:y+h,x:x+w])
        cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),(0,0,255))
    cv2.imshow("Face",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
