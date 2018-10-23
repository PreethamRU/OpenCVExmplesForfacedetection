import cv2
import sys

faceCascade = cv2.CascadeClassifier('C:\\Users\\Admin\\Desktop\\opencv\\opencv\\data\\haarcascades\\haarcascade_frontalface_default.xml')


video_capture = cv2.VideoCapture(0)

while True:

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3,5)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('c'):
        crop_img = frame[y: y + h, x: x + w] # Crop from x, y, w, h -> 100, 200, 300, 400
        cv2.imwrite("C:\\Users\\Admin\\Desktop\\opencv\\New folder\\temporarystore.jpg", crop_img)
        break
video_capture.release()
cv2.destroyAllWindows()
