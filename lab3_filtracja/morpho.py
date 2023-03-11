import cv2
import numpy as np
from matplotlib import pyplot as plt



cv2.namedWindow('image')
img=cv2.imread('./Images/lenna_noise.bmp')
img2=cv2.imread('./Images/lenna_salt_and_pepper.bmp')
th_val=80

def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {2*value+1}')
    pass



ret,img_bin=cv2.threshold(img,th_val,255,cv2.THRESH_BINARY)
thresh=cv2.createTrackbar('TH', 'image', 0, 50, empty_callback)

while True:


    th = cv2.getTrackbarPos('TH', 'image')

    kernel = np.ones((2*th+1,2*th+1),np.uint8)
    img_erode=cv2.erode(img_bin,kernel,iterations = 1)
    img_dilate=cv2.dilate(img_bin,kernel,iterations = 1)
    img_open=cv2.morphologyEx(img_bin,cv2.MORPH_OPEN,kernel)
    img_close=cv2.morphologyEx(img_bin,cv2.MORPH_CLOSE,kernel)
    
    cv2.imshow('image', img_bin)
    cv2.imshow('erode', img_erode)
    cv2.imshow('dilate', img_dilate)
    cv2.imshow('MORPH_OPEN', img_open)
    cv2.imshow('MORPH_CLOSE', img_close)









    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break
   


cv2.destroyAllWindows()