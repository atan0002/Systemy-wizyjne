import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()






while True:

    ret, frame = cap.read()

    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV, (90, 50, 70), (100, 255, 255))

    cv.imshow('frame_threshold', frame_threshold)
    cv.imshow('frame', frame)


    if cv.waitKey(1) == ord('q'):
        break



cap.release()
cv.destroyAllWindows()