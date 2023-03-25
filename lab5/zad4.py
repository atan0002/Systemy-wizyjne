import cv2 
import numpy as np

img = cv2.imread('./Images/drone_ship.jpg')
img2=img.copy()

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2 = cv2.medianBlur(gray,5)
cimg = cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)


circles = cv2.HoughCircles(img2,cv2.HOUGH_GRADIENT,1.1,70,
                            param1=250,param2=60,minRadius=35,maxRadius=0)


circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)


while True:
   
  

    cv2.imshow('detected circles',cimg)
   
    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break
