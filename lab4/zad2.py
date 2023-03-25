import cv2
import numpy as np
 

cv2.namedWindow('image')
cap = cv2.imread('./Images/road.jpg')
cap=cv2.resize(cap,(600,500),interpolation = cv2.INTER_AREA)


points=list()
counter=0
set_persp=False


def mouse_callback(event,x,y,flags,param):
    global counter,points,set_persp

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append(x)
        points.append(y)
        counter+=1
        if counter==4:
            set_persp=True
    

cv2.setMouseCallback('image',mouse_callback)  



while True:
     
   
 
    # Locate points of the documents
    # or object which you want to transform
     
    # Apply Perspective Transform Algorithm
    cv2.imshow('image',cap)

    if set_persp:

        points=np.asarray(points,dtype=np.float32)
        points=points.reshape(4,2)
        pst1=points
        pst2=np.float32([[200,500],[400,500],[200,0],[400,0]])        
    
        matrix = cv2.getPerspectiveTransform(pst1,pst2)
        result = cv2.warpPerspective(cap, matrix, (600, 500))
        cap=result
        set_persp=False
        
        # cv2.imshow('frame', frame) # Initial Capture

        # cv2.imshow('frame1', result) # Transformed Capture
     
    # Wrap the transformed image
 
 
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()