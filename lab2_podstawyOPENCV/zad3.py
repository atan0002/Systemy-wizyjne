import cv2
import numpy as np

from time import perf_counter

photo=cv2.imread('./Images/qr.jpg')

tL_start=perf_counter()
inter_linear = cv2.resize(photo, (0, 0), fx=2.75, fy=2.75,interpolation=cv2.INTER_LINEAR)
tL_stop=perf_counter()
elapsed_TL=tL_stop-tL_start

tN_start=perf_counter()
inter_nearest = cv2.resize(photo, (0, 0), fx=2.75, fy=2.75,interpolation=cv2.INTER_NEAREST)
tN_stop=perf_counter()
elapsed_TN=tN_stop-tN_start

tA_start=perf_counter()
inter_area = cv2.resize(photo, (0, 0), fx=2.75, fy=2.75,interpolation=cv2.INTER_AREA)
tA_stop=perf_counter()
elapsed_TA=tA_stop-tA_start

tLA_start=perf_counter()
inter_LANCZO = cv2.resize(photo, (0, 0), fx=2.75, fy=2.75,interpolation=cv2.INTER_LANCZOS4)
tLA_stop=perf_counter()

elapsed_TLA=tLA_stop-tLA_start

print('Time elapsed for INTER_LINEAR',elapsed_TL)
print('Time elapsed for INTER_NEAREST',elapsed_TN)
print('Time elapsed for INTER_AREA',elapsed_TA)
print('Time elapsed for INTER_LANCZOS4',elapsed_TLA)



while True:

    cv2.imshow('orginal', photo)
    cv2.imshow('INTER_LINEAR', inter_linear)
    cv2.imshow('inter_nearest', inter_nearest)
    cv2.imshow('INTER_AREA', inter_area)
    cv2.imshow('INTER_LANCZOS4', inter_LANCZO)


    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break
   

cv2.destroyAllWindows()