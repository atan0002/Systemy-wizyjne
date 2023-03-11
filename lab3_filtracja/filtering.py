import cv2
import numpy as np
from matplotlib import pyplot as plt


def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {2*value+1}')
    pass


cv2.namedWindow('image')
img=cv2.imread('./Images/lenna_noise.bmp')
img2=cv2.imread('./Images/lenna_salt_and_pepper.bmp')
thresh=cv2.createTrackbar('TH', 'image', 0, 50, empty_callback)



while True:

    

    th = cv2.getTrackbarPos('TH', 'image')

    #filtr uśredniajcy
    blur=cv2.blur(img,(th*2+1,th*2+1)) 
    blur2=cv2.blur(img2,(th*2+1,th*2+1)) 

    #filtr medianowy 
    median= cv2.medianBlur(img,th*2+1)
    median2= cv2.medianBlur(img2,th*2+1)

    #filtr gaussowski

    gauss=cv2.GaussianBlur(img,(th*2+1,th*2+1),0)
    gauss2=cv2.GaussianBlur(img2,(th*2+1,th*2+1),0)


    cv2.imshow('image', img)
    cv2.imshow('Blur method - noise', blur)
    cv2.imshow('Median - noise', median)
    cv2.imshow('Gauss - noise', gauss)
    cv2.imshow('Blur method - salt & pepper', blur2)
    cv2.imshow('Median - salt & pepper', median2)
    cv2.imshow('Gauss - salt & pepper', gauss2)
    
    


    # plt.subplot(221),plt.imshow(img),plt.title('Original')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(222),plt.imshow(blur),plt.title('Blurred')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(223),plt.imshow(median),plt.title('Median')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(224),plt.imshow(gauss),plt.title('Gauss')
    # plt.xticks([]), plt.yticks([])

    # plt.show()


    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break
   

cv2.destroyAllWindows()


# szum lepiej filtruje filtr gausowski
#zakłocenia typu salt and pepper lepiej filtruje filtr medianowy