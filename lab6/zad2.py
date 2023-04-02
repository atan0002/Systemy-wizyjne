import cv2
from matplotlib import pyplot as plt
import numpy as np

img=cv2.imread('./Images/pug.png')
img=cv2.resize(img,(600,500))

img3=img.copy()

img2=img.copy()
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img2_detect=img2[20:185,100:255]
meth=1

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
methods_names = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']


res = cv2.matchTemplate(img2,img2_detect,methods[meth])
threshold = 0.1
loc = np.where( res >= threshold)

# cv2.imshow('detect',loc[::-1])
# cv2.waitKey(0)


min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
w, h = img2_detect.shape[::-1]

# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if methods[0] in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img,top_left, bottom_right, 255, 2)


plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(methods_names[meth])

for pt in zip(*loc[::-1]):
    cv2.rectangle(img3, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

plt.figure(2)
plt.imshow(img3)
# cv2.imshow('orginal',img)
# cv2.imshow('detected',img3)
# cv2.waitKey(0)
plt.show()



# img_detect