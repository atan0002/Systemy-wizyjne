import cv2 
import numpy as np

img=cv2.imread('./Images/not_bad.jpg',cv2.IMREAD_GRAYSCALE)

img=cv2.resize(img,(600,500))
img2=cv2.imread('./Images/not_bad.jpg')
img2=cv2.resize(img2,(600,500))

ret, thresh1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

kernel=np.ones((5,5))

img_ = cv2.dilate(thresh1, kernel)

contours, hierarchy = cv2.findContours(img_, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contours=contours[1:5]
img2=cv2.drawContours(img2, contours,-1, (255,0,255), 3)

moments=list()

for i in contours:
    moments.append(cv2.moments(i))


centeroids=dict()
#momemnty
for i in range(0,len(moments)):
    up={f"M{i}":{"cx":moments[i]["m10"]/moments[i]["m00"],"cy":moments[i]["m01"]/moments[i]["m00"]}}
    centeroids.update(up)
# powierzchnia konturu
# area=cv2.contourArea(contours[0])
# print()

pts1 = np.float32([[centeroids['M0']['cx'],centeroids['M0']['cy']], [centeroids['M1']['cx'],centeroids['M1']['cy']],
                       [centeroids['M2']['cx'],centeroids['M2']['cy']], [centeroids['M3']['cx'],centeroids['M3']['cy']]])
pts2 = np.float32([[img.shape[1], img.shape[0]],[0,img2.shape[0]],[img2.shape[1],0],[0, 0]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(img2, matrix, (600, 500))

cv2.imshow('contours',result)
#cv2.imshow('thresh',thresh1)

cv2.waitKey(0)