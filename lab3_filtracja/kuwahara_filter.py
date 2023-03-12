import cv2
import numpy as np
from matplotlib import pyplot as plt



img=cv2.imread('./Images/lenna.png',cv2.IMREAD_GRAYSCALE)

def img_white_pix(img_):
    
    img_white=img_.copy()
    rows=img_white.shape[0]
    columns=img_white.shape[1]
    
    for i in range(0,rows,3):
        third_j=0
        for j in range(columns):
            
            if ((j+1)-third_j)==3:
                img_white[i,j]=255

                third_j=j+1

    return img_white


def kuwahara_filter(w,imgl):

    width=w
    L=int((width-1)/2)
    region_width=width-L
    rows=imgl.shape[0]
    columns=imgl.shape[1]
    img2=imgl.copy()
    stat={'mean':list(),'deviat':list()}



    for i in range(1,rows-width):

        for j in range(1,columns-width):
            
            window=imgl[i:i+width,j:j+width]
            rows_w=window.shape[0]
            columns_w=window.shape[1]
            region1=window[0:region_width,0:region_width]
            regs=region1.shape

            reg1mean,reg1stddev=cv2.meanStdDev(region1)
       
            stat['mean'].append(reg1mean[0][0])
            stat['deviat'].append(reg1stddev[0][0])
            region2=window[0:region_width,region_width-1:columns_w]
            reg2mean,reg2stddev=cv2.meanStdDev(region2)

            regs=region2.shape
            
            stat['mean'].append(reg2mean[0][0])
            stat['deviat'].append(reg2stddev[0][0])
            region3=window[region_width-1:rows_w,region_width-1:columns_w]
            reg3mean,reg3stddev=cv2.meanStdDev(region3)

            regs=region3.shape

            stat['mean'].append(reg3mean[0][0])
            stat['deviat'].append(reg3stddev[0][0])
            region4=window[region_width-1:rows_w,0:region_width]
            reg4mean,reg4stddev=cv2.meanStdDev(region4)
            stat['mean'].append(reg4mean[0][0])
            stat['deviat'].append(reg4stddev[0][0])

            regs=region4.shape


            min_dev_ind=stat['deviat'].index(min(stat['deviat']))

            img2[i+L,j+L]=stat['mean'][min_dev_ind]
            stat['mean'].clear()
            stat['deviat'].clear()

    return img2 


imgW=img_white_pix(img)

img_kuh=kuwahara_filter(5,imgW)

while True:
    
    cv2.imshow('image', img)
    
    cv2.imshow('Kuhwara filter',img_kuh)

    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break        





