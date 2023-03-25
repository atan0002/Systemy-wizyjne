import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread('./Images/lenna.png',cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('image')


def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    pass

cv2.createTrackbar('H', 'image', 0, 255, empty_callback)
cv2.createTrackbar('L', 'image', 0, 255, empty_callback)
# Setting parameter values
t_lower = 50  # Lower Threshold
t_upper = 150  # Upper threshold
  



while True:
    t_lower = cv2.getTrackbarPos('L', 'image')
    t_upper = cv2.getTrackbarPos('H', 'image')
   
    edge = cv2.Canny(img, t_lower, t_upper)
  

    cv2.imshow('image', img)
    cv2.imshow('edge', edge)
   
    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break

    # get current positions of four trackbars
    
    

    


cv2.destroyAllWindows()