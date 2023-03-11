import cv2


cv2.namedWindow('image')

#wczytanie
photo=cv2.imread('./Images/zdjecie.jpeg')
#konwersja do skali szarości
photo_GS = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
#progowanie binarne 


def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    pass

def empty_callback2(value):
    print(f'Trackbar reporting for duty with value: {whichMethod(value)}')
    pass

def whichMethod(val):
   
    methods=['THRESH_BINARY','THRESH_BINARY_INV','THRESH_TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV']
    method=methods[val]
    return method






thresh_val=cv2.createTrackbar('GS', 'image', 177, 255, empty_callback)
threshold_method=cv2.createTrackbar('MN', 'image', 0, 4, empty_callback2)

map_functions={'THRESH_BINARY': cv2.THRESH_BINARY,'THRESH_BINARY_INV': cv2.THRESH_BINARY_INV,'THRESH_TRUNC': cv2.THRESH_TRUNC,
 'THRESH_TOZERO': cv2.THRESH_TOZERO,'THRESH_TOZERO_INV': cv2.THRESH_TOZERO_INV}



gs_val=177

while True:

    mn_val = cv2.getTrackbarPos('MN', 'image')    #method name


    ret,thresh1 = cv2.threshold(photo_GS,gs_val,255,map_functions[whichMethod(mn_val)])
  

    cv2.imshow('image', thresh1)
    gs_val = cv2.getTrackbarPos('GS', 'image')


    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break
   
   


cv2.destroyAllWindows()