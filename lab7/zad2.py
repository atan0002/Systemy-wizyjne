import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

ret, previous_frame = cap.read()

previous_frame = cv.cvtColor(previous_frame, cv.COLOR_BGR2GRAY)

current_frame=None
next_frame=None


ret, current_frame = cap.read()

current_frame = cv.cvtColor(current_frame, cv.COLOR_BGR2GRAY)
kernel = np.ones((5,5),np.uint8)

def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    pass



cv.namedWindow('result')
cv.createTrackbar('res', 'result', 50, 255, empty_callback)


while True:

 



    ret, next_frame = cap.read()

    next_frame = cv.cvtColor(next_frame, cv.COLOR_BGR2GRAY)





    # cv.imshow('previous frame', previous_frame)
    # cv.imshow('current frame', current_frame)
    # cv.imshow('next frame', next_frame)

    deltaI1=np.absolute(next_frame-current_frame)

    deltaI2=np.absolute(next_frame-previous_frame)


    deltaI=cv.bitwise_and(deltaI1,deltaI2)

    closing = cv.morphologyEx(deltaI, cv.MORPH_CLOSE, kernel)

    res = cv.getTrackbarPos('res', 'result')
    ret,diff = cv.threshold(closing, res, 255, cv.THRESH_BINARY)

    cv.imshow('result', diff)








    previous_frame=current_frame
    current_frame=next_frame



 
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()

