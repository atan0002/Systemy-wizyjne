import cv2
import numpy as np
from matplotlib import pyplot as plt



img=cv2.imread('./Images/whitepixels.png')


def kuwahara_filter(L,imgl):

    width=2*L+1
    region_width=width-L
    rows=imgl.shape[0]
    columns=imgl.shape[1]
    img2=imgl.copy()
    stat={'mean':list(),'deviat':list()}



    for i in range(1,rows-L-1):

        for j in range(1,columns-L-1):
            
            window=imgl[i:i+width,j:j+width]
            rows_w=window.shape[0]
            columns_w=window.shape[1]
            region1=window[0:region_width,0:region_width]
            reg1mean,reg1stddev=cv2.meanStdDev(region1)
       
            stat['mean'].append(reg1mean[0][0])
            stat['deviat'].append(reg1stddev[0][0])
           
            region2=window[0:region_width,region_width-1:columns_w]
            reg2mean,reg2stddev=cv2.meanStdDev(region2)
            stat['mean'].append(reg2mean[0][0])
            stat['deviat'].append(reg2stddev[0][0])
            region3=window[region_width-1:rows_w,region_width-1:columns_w]
            reg3mean,reg3stddev=cv2.meanStdDev(region3)
            stat['mean'].append(reg3mean[0][0])
            stat['deviat'].append(reg3stddev[0][0])
            region4=window[region_width-1:rows_w,0:region_width]
            reg4mean,reg4stddev=cv2.meanStdDev(region4)
            stat['mean'].append(reg4mean[0][0])
            stat['deviat'].append(reg4stddev[0][0])


            min_dev_ind=stat['deviat'].index(min(stat['deviat']))

            img2[i+L,j+L]=stat['mean'][min_dev_ind]
            stat['mean'].clear()
            stat['deviat'].clear()

    return img2 

img_kuh=kuwahara_filter(2,img)

while True:
    
    cv2.imshow('image', img)
    
    cv2.imshow('Kuhwara filter',img_kuh)

    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break        





