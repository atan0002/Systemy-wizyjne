import numpy as np
import cv2 
from matplotlib import pyplot as plt


points=list()
counter=0
set_persp=False

cv2.namedWindow('image')


img = cv2.imread('./Images/road.jpg')
img=cv2.resize(img,(600,500),interpolation = cv2.INTER_AREA)
# img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
assert img is not None, "file could not be read, check with os.path.exists()"
# hist = cv2.calcHist([img],[0],None,[256],[0,256])
# plt.subplot(1, 2, 1)
# plt.hist(img.ravel(),256,[0,256])
# plt.subplot(1, 2, 2)
# plt.imshow(img)
# plt.show()


def mouse_callback(event,x,y,flags,param):
    global counter,points,set_persp

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append(x)
        points.append(y)
        counter+=1
        if counter==1:
            set_persp=True
    


cv2.setMouseCallback('image',mouse_callback)  

while True:

    

    if set_persp:

        points.append(points[0]+50)
        points.append(points[1])

        points.append(points[0])
        points.append(points[1]+50)
        points.append(points[2])
        points.append(points[3]+50)
        
        # points=np.asarray(points,dtype=np.float32)
        # points=points.reshape(4,2)
        # print(points[0],points[2],points[1],points[5])
        frame=img[points[1]:points[5],points[0]:points[2]]

        # frame_HSV = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
        frame_threshold = cv2.inRange(frame,  (36, 25, 25), (70, 255,255))
        # cv2.imshow('result',frame_threshold)

        counter=0
        img[points[1]:points[5],points[0]:points[2],2]=np.zeros(frame_threshold.shape)
        img[points[1]:points[5],points[0]:points[2],0]=np.zeros(frame_threshold.shape)
        img[points[1]:points[5],points[0]:points[2],1]=frame_threshold
        points.clear()
        set_persp=False
    

    cv2.imshow('image',img)

    k = cv2.waitKey(1) & 0xFF
    
    if k == 27:
        break


cv2.destroyAllWindows()