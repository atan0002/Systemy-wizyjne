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
cv.createTrackbar('ForeGround', 'foreground image', 50, 255, empty_callback)
model_back=None
current=None
diff=None

kernel = np.ones((3, 3), np.uint8)


def medianApprox(background, foreground):

    np.where(background<foreground,background+1,background)
    np.where(background>foreground,background-1,background)
    
    # for i in range(background.shape[1]):
    #     for j in range(background.shape[0]):

    #         if background[j][i]<foreground[j][i]:
    #             background[j][i]+=1
            
    #         elif background[j][i]>foreground[j][i]:
    #                background[j][i]-=1

    return background

first_pixels=list()
changed_pixels=list()


def countPixels(img,changed):
    k=0
    # np.where(img==255,k+1,k)
    for i in range(img.shape[1]):
        for j in range(img.shape[0]):

            if img[j][i]==255:
                k+=1
                changed.append((i,j))
                


    return k


def setAlarm(count,ref):
    alarm=False
    if count>ref+ref*0.5:
        alarm=True

    return alarm

def findRec(changed,w):

    start=w/2
    over=w/2

    start_point=None
    over_point=None

    for i in range(1,len(changed)):

        if(changed[i][1]<start):
            start_point=(changed[i][0],changed[i][1])
            start=changed[i][1]
        elif(changed[i][1]>over):
            over_point=(changed[i][0],changed[i][1])
            over=changed[i][1]

    return [start_point,over_point]









# #mieszaniniy gaussowskie
# backSub = cv.createBackgroundSubtractorMOG2()
backSub = cv.createBackgroundSubtractorKNN()


# def count_changes():
first_count_of_pixels=None


while True:

    
    # Capture frame-by-frame        qq
    ret, model_back = cap.read()
    # if frame is read correctly ret is True
    
    # Our operations on the frame come here
    model_back = cv.cvtColor(model_back, cv.COLOR_BGR2GRAY)

    #new model_back

    if current is not None:
        model_back=medianApprox(model_back,current)
   
   
    if model_back is not None:
    # Capture frame-by-frame        qq
        ret, current = cap.read()
        current = cv.cvtColor(current, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
       
        diff=cv.absdiff(model_back,current)


    if diff is not None:
       
            

        foreGround = cv.getTrackbarPos('ForeGround', 'foreground image')
        diff = cv.morphologyEx(diff, cv.MORPH_CLOSE, kernel, iterations=1)
        ret,diff = cv.threshold(diff, foreGround, 255, cv.THRESH_BINARY)

        if first_count_of_pixels is None:
            first_count_of_pixels=countPixels(diff,first_pixels)
            print(first_count_of_pixels)

        count=countPixels(diff,changed_pixels)
        alarm=setAlarm(count,first_count_of_pixels)
        if alarm:

            print("Alarm set true")
            rec=findRec(changed_pixels,current.shape[0])

            cv.rectangle(current,rec[0],rec[1],255,2)

            cv.imwrite('./intruz.png',current)


    cv.imshow('current image', current)

        

        
       
    #     cv.imshow('foreground image', diff)

    # diff=backSub.apply(model_back)


    # cv.rectangle(model_back, (10, 2), (100,20), (255,255,255), -1)
    # cv.putText(model_back, str(cap.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
   
    cv.imshow('background image', model_back)


    cv.imshow('foreground image', diff)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()