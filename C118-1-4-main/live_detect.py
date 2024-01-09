import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#host do video

video = cv2.VideoCapture(0)

while(True):
    ret, frame = video.read()

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostos = face_cascade.detectMultiScale(cinza, 1.1, 5)

    for(x, y, w, h) in rostos:
        cv2.rectangle(frame, (x, y), (x + w, y + h),(255, 0, 0), 3)

    cv2.imshow('frame', frame)

    if cv2.waitKey(25) == 32:
        break

video.release()

cv2.destroyAllWindows()