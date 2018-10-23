import cv2
import numpy as np
import time

face_cascade = cv2.CascadeClassifier('C:\\Users\\Admin\\Desktop\\opencv\\opencv\\data\\haarcascades\\haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('C:\\Users\\Admin\\Desktop\\opencv\\opencv\\data\\haarcascades\\haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
	print len(faces)
    for(x,y,w,h) in faces:
        crop_img = img[y: y + h, x: x + w] # Crop from x, y, w, h -> 100, 200, 300, 400
        ts = time.time()
        'cv2.imwrite("C:\\Users\\Admin\\Desktop\\opencv\\detectedfaces\\"+str(ts)+".jpg", crop_img)'
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h,x:x+h]
        roi_color = img[y:y+h,x:x+h]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
                 cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
    cv2.imshow('img',img)
    time.sleep(5)
    k = cv2.waitKey(1) & 0xFF == ord('q')
    if k == 27:
        break;

cap.release()
cv2.destroAllWindows()
