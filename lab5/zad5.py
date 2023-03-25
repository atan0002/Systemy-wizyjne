import cv2 
import numpy as np


img = cv2.imread('./Images/fruit.jpg')
img2=img.copy()


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2 = cv2.medianBlur(gray,5)
cimg = cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)


def find_circle(img):
    imgc=img.copy()
    circles = cv2.HoughCircles(imgc,cv2.HOUGH_GRADIENT,1.25,70,
                            param1=250,param2=40,minRadius=35,maxRadius=0)
    
    return circles


def draw_circle(cimg,circles,r,g,b):
    circles = np.uint16(np.around(circles))
    img_=cimg.copy()

    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(img_,(i[0],i[1]),i[2],(r,g,b),2)
        # draw the center of the circle
        cv2.circle(img_,(i[0],i[1]),2,(0,0,255),3)
    
    return img_

#przeszukanie przez HSV 
frame_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
frame_th_green = cv2.inRange(frame_HSV, (36, 15, 15), (70, 255,255))
frame_th_orange = cv2.inRange(frame_HSV, (5,42,42), (15,255,255))

#inwersja mask (czarno biale) odpowiednio wykrytych kolorów na poczatku, a pozniej polaczenie z tłem i konwersja do szarego zdjecia

mask_inv = cv2.bitwise_not(frame_th_green)
img2_fg_green = cv2.bitwise_and(img,img,mask = frame_th_green)
gray_gr = cv2.cvtColor(img2_fg_green,cv2.COLOR_BGR2GRAY)
frame_th_green= cv2.medianBlur(gray_gr,3)

mask_inv2 = cv2.bitwise_not(frame_th_orange)
img2_fg_orange = cv2.bitwise_and(img,img,mask = frame_th_orange)
gray_or = cv2.cvtColor(img2_fg_orange,cv2.COLOR_BGR2GRAY)
frame_th_orange= cv2.medianBlur(gray_or,3)




cr_green=find_circle(frame_th_green)
# print(cr_green)
cr_orange=find_circle(frame_th_orange)

result=draw_circle(img,cr_green,55,15,100)
result=draw_circle(result,cr_orange,255,0,0)

while True:

    
    
    cv2.imshow('test',img2_fg_orange)
    cv2.imshow('roi',result)
    # cv2.imshow('green',frame_th_green)
    # cv2.imshow('orange',frame_th_orange)

    # cv2.imshow('detected circles',result)
   
    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break
