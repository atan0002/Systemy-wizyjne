import cv2 
import numpy as np


img = cv2.imread('./Images/shapes.jpg')
img2=img.copy()

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
lines = cv2.HoughLines(edges,1,np.pi/180,200)
img2 = cv2.medianBlur(gray,5)
cimg = cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

circles = cv2.HoughCircles(img2,cv2.HOUGH_GRADIENT,1,20,
                            param1=70,param2=40,minRadius=10,maxRadius=0)


circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)


while True:
   
  
  

    cv2.imshow('detected lines', img)
    # cv2.imshow('lines', edge)
    cv2.imshow('detected circles',cimg)
   
    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break

