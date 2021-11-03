import cv2
import os
def deepfire_CV(frame):
    fire_cascade = cv2.CascadeClassifier(os.getcwd()+"\WEB\\"+"view\WebCamera\models\\"+"fire_detection.xml")

    # cap = cv2.VideoCapture(0)

    while (True):
        # ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

        for (x, y, w, h) in fire:
            cv2.rectangle(frame, (x - 20, y - 20), (x + w + 20, y + h + 20), (255, 0, 0), 2)
            # roi_gray = gray[y:y + h, x:x + w]
            # roi_color = frame[y:y + h, x:x + w]
            print("불 감지")


        return frame