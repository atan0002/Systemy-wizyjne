import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread('./Images/lenna.png',cv2.IMREAD_GRAYSCALE)

# img=np.abs(img)

kernelPrewittX = np.float32([[1,0,-1],[1,0,-1],[1,0,-1]])/3
kernelPrewittY = np.float32([[1,1,1],[0,0,0],[-1,-1,-1]])/3
kernelSobelX = np.float32([[1,0,-1],[2,0,-2],[1,0,-1]])/4
kernelSobelY = np.float32([[1,2,1],[0,0,0],[-1,-2,-1]])/4

img_PrewittX = cv2.filter2D(src=img, ddepth=cv2.CV_32F, kernel=kernelPrewittX)
img_SobelX = cv2.filter2D(src=img, ddepth=cv2.CV_32F, kernel=kernelSobelX)
img_PrewittY = cv2.filter2D(src=img, ddepth=cv2.CV_32F, kernel=kernelPrewittY)
img_SobelY = cv2.filter2D(src=img, ddepth=cv2.CV_32F, kernel=kernelSobelY)
img_Prewitt=np.sqrt(np.power(img_PrewittX,2)+np.power(img_PrewittY,2))
img_Sobel=np.sqrt(img_SobelX**2+img_SobelY**2)

img_Prewitt_mod=np.arctan(img_PrewittY/img_PrewittX)
img_Prewitt=np.abs(img_Prewitt)
img_Prewitt=img_Prewitt.astype(dtype=np.uint8)

img_Sobel_mod=np.arctan(img_SobelY/img_SobelX)

img_Sobel=np.abs(img_Sobel)
img_Sobel=img_Sobel.astype(dtype=np.uint8)

cv2.imshow('Original', img)
cv2.imshow('Img Prewitt', img_Prewitt)
cv2.imshow('Img Sobel', img_Sobel) 
cv2.imshow('Img Sobel mod', img_Sobel_mod.astype(dtype=np.uint8)) 
cv2.imshow('Img Prewitt mod', img_Prewitt_mod.astype(dtype=np.uint8)) 

cv2.waitKey()
cv2.destroyAllWindows()