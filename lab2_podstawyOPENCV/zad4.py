import cv2
import numpy as np

cv2.namedWindow('image')

img1=cv2.imread('./Images/qr.jpg')
img2=cv2.imread('./Images/PUTVISION_LOGO.png')

# print(img2.shape[0])

img1 = cv2.resize(img1, dsize=(img2.shape[0], img2.shape[1]),interpolation=cv2.INTER_LINEAR)

def empty_callback(value):
    print(f'Trackbar reporting for duty with alpha value: {value}')
    pass

def empty_callback2(value):
    print(f'Trackbar reporting for duty with beta value: {value}')
    pass

alpha_val=cv2.createTrackbar('AL', 'image', 0, 100, empty_callback)
beta_val=cv2.createTrackbar('BE', 'image', 0, 100, empty_callback2)



while True:

    alpha=cv2.getTrackbarPos('AL', 'image') 
    beta=cv2.getTrackbarPos('BE', 'image') 

    dst = cv2.addWeighted(img1,alpha/100,img2,beta/100,0)

    cv2.imshow('image',dst)
    

    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break



cv2.destroyAllWindows()