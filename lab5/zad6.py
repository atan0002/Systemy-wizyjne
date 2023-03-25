import cv2 
import numpy as np

img = cv2.imread('./Images/coins.jpg')
img2=img.copy()


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2 = cv2.medianBlur(gray,5)
cimg = cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)

def find_circle(img,min_rad,max_rad):
    imgc=img.copy()
    circles = cv2.HoughCircles(imgc,cv2.HOUGH_GRADIENT,1.25,70,
                            param1=250,param2=45,minRadius=min_rad,maxRadius=max_rad)
    
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



tens=find_circle(img2,30,50)


result=draw_circle(img,tens,0,0,255)

zloty=find_circle(img2,80,150)


result=draw_circle(result,zloty,255,0,255)

count_tens=len(tens[0])
count_zloty=len(zloty[0])
cost=count_zloty*1+count_tens*0.1
print('Dziesiatki',count_tens)
print('Zlotowki',count_zloty)
print('Kwota','%.2f'%cost)


while True:

    
    cv2.imshow('result',result)
    # cv2.imshow('green',frame_th_green)
    # cv2.imshow('orange',frame_th_orange)

    # cv2.imshow('detected circles',result)
   
    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break



