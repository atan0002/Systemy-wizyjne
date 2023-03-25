import cv2
import numpy as np
 

cv2.namedWindow('image')
cap = cv2.imread('./Images/gallery.png')
# cap=cv2.resize(cap,(600,500),interpolation = cv2.INTER_AREA)
mops = cv2.imread('./Images/pug.png')

points=list()
counter=0
set_persp=False


def mouse_callback(event,x,y,flags,param):
    global counter,points,set_persp

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append(x)
        points.append(y)
        counter+=1
        if counter==3:
            set_persp=True
    

cv2.setMouseCallback('image',mouse_callback)  



while True:
     
   
 
    # Locate points of the documents
    # or object which you want to transform
     
    # Apply Perspective Transform Algorithm
    cv2.imshow('image',cap)
    # cv2.imshow('mops',mops)

    if set_persp:

        # points=np.asarray(points,dtype=np.float32)
        # points=points.reshape(4,2)
        # points.append(points[0]+50)
        # points.append(points[1])

        # points.append(points[0])
        # points.append(points[1]+50)
        # cv2.imshow('mops2',mops)

        pnts_copy=points.copy()

        

        x=points[2]-points[0]
        y=points[5]-points[1]

        points[4]=points[0]-points[4]
        points[5]=points[5]-points[1]
        points[0]=0
        points[2]=x
        points[3]=points[1]-points[3]
       
        points[1]=0
        
       
        # mops=cv2.resize(mops,(x,y),interpolation = cv2.INTER_AREA) #lewy-prawy gorny, lewy -prawy dolny
        # cv2.imshow('mops',mops)

        points[4]=points[0]
        # points.append(points[4]+x)
        # points.append(points[5]+y)

        pst2=np.asarray(points)
        pst2=pst2.astype(np.float32)
        pst2=pst2.reshape(3,2)

        # pst1=np.float32([[300,600],[300+mops.shape[0],600],[300,600+mops.shape[1]]])        
        pst1=np.float32([[0,0],[mops.shape[0],0],[0,mops.shape[1]]])

        M = cv2.getAffineTransform(pst1,pst2)
        mops = cv2.warpAffine(mops,M,(x+20,y))
        # cv2.imshow('roi',mops)
        # cap=result
        set_persp=False

        img2gray = cv2.cvtColor(mops,cv2.COLOR_BGR2GRAY)

        
      
        ret, mask = cv2.threshold(img2gray, 50, 250, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        mask_inv=mask_inv[0:y,0:x+20]
        cv2.imshow('roi',mask_inv)
        

        roi = cap[pnts_copy[1]:pnts_copy[5],pnts_copy[0]:pnts_copy[2]+20]
        
        cap_h = cv2.bitwise_and(roi,roi,mask = mask_inv)
        cv2.imshow('mops',mops)

        # cap=cv2.addWeighted(img1,0.7,img2,0.3,0)
        
        img2_fg = cv2.bitwise_and(mops,mops,mask = mask)
        # Put logo in ROI and modify the main image
        dst = cv2.add(cap_h,img2_fg)
        # dst = cv2.addWeighted(cap_h,0.2,img2_fg,0.8,0)
        cap[pnts_copy[1]:pnts_copy[5],pnts_copy[0]:pnts_copy[2]+20] = dst



        # cap[pnts_copy[1]:pnts_copy[5],pnts_copy[0]:pnts_copy[2]]=mops
        points.clear()
       
        
        # cv2.imshow('frame', frame) # Initial Capture

        # cv2.imshow('frame1', result) # Transformed Capture
     
    # Wrap the transformed image
 
 
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()