import cv2
import numpy as np
from matplotlib import pyplot as plt
from time import perf_counter


img=cv2.imread('./Images/lenna_noise.bmp')
img_white=img.copy()
img_av=img.copy()
rows=img.shape[0]
columns=img.shape[1]

third_j=0


for i in range(rows):
    for j in range(columns):
        
        if ((j+1)-third_j)==3:
            img_white[i,j]=[255,255,255]

            third_j=j+1

column=1



def imgblur(img):
    img2=img.copy()
    for i in range(2,rows-2):

        for j in range(2,columns-2):

            c1=np.mean(img[i-1:i+1,j-1:j+1])
            img2[i,j]=c1
    
    return img2

tS_start=perf_counter()
img_av=imgblur(img_av)

tS_stop=perf_counter()

print(f'Self-implementation:{tS_stop-tS_start}')



tB_start=perf_counter()
img_blur=cv2.blur(img, (3, 3))
tB_stop=perf_counter()
print(f'Blur:{tB_stop-tB_start}')

tf_start=perf_counter()
kernel=np.ones((3,3),np.float32)/9
img_f=cv2.filter2D(img,ddepth=-1,kernel=kernel)
tf_stop=perf_counter()
print(f'Filter:{tf_stop-tf_start}')




while True:
    cv2.imshow('Orginal', img)
    cv2.imshow('Image white', img_white)
    cv2.imshow('Image av',img_av)
    cv2.imshow('Image blur', img_blur)
    cv2.imshow('Image filter', img_f)
    

    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break