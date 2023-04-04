import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

ret, frame = cap.read()
# if frame is read correctly ret is True
# Our operations on the frame come here
gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
# Display the resulting frame
cv.imshow('current image', gray)


def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    pass

cv.namedWindow('foreground image')
cv.createTrackbar('ForeGround', 'foreground image', 0, 255, empty_callback)
model_back=None
current=None
diff=None

kernel = np.ones((3, 3), np.uint8)


def medianApprox(background, foreground):
    
    for i in range(background.shape[1]):
        for j in range(background.shape[0]):

            if background[j][i]<foreground[j][i]:
                background[j][i]+=1
            
            elif background[j][i]>foreground[j][i]:
                   background[j][i]-=1

    return background
        

# #mieszaniniy gaussowskie
# backSub = cv.createBackgroundSubtractorMOG2()
backSub = cv.createBackgroundSubtractorKNN()


# def count_changes():


while True:

    
    # Capture frame-by-frame        qq
    ret, model_back = cap.read()
    # if frame is read correctly ret is True
    
    # Our operations on the frame come here
    model_back = cv.cvtColor(model_back, cv.COLOR_BGR2GRAY)

    #new model_back

    # if current is not None:
    #     model_back=medianApprox(model_back,current)
   
   
    # if model_back is not None:
    # # Capture frame-by-frame        qq
    #     ret, current = cap.read()
    #     current = cv.cvtColor(current, cv.COLOR_BGR2GRAY)
    #     # Display the resulting frame
    #     cv.imshow('current image', current)
    #     diff=cv.absdiff(model_back,current)


    # if diff is not None:
       
            

    #     foreGround = cv.getTrackbarPos('ForeGround', 'foreground image')
    #     diff = cv.morphologyEx(diff, cv.MORPH_CLOSE, kernel, iterations=1)
    #     ret,diff = cv.threshold(diff, foreGround, 255, cv.THRESH_BINARY)
        
       
    #     cv.imshow('foreground image', diff)

    diff=backSub.apply(model_back)


    # cv.rectangle(model_back, (10, 2), (100,20), (255,255,255), -1)
    # cv.putText(model_back, str(cap.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
   
    cv.imshow('background image', model_back)


    cv.imshow('foreground image', diff)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()