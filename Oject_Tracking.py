"""
THIS PROGRAM IS CREATED BY Aakasha01Agarwal
THE RESULT SCREEN WILL SHOW YOU THE OUTPUT OF THE DESIRED COLOUR TRACKING
PRESS ESC TO QUIT
CHANGE THE TRACKBAR VALUES OF THE LOWER BOUND HSV TO OBTAIN THE DESIRED COLOUR
"""

import cv2 as cv
import numpy as np

def nothing(x):
    pass


cv.namedWindow("Tracking")                             #named window

# CREATING TRACKBARS TO GET THE LOWER VALUES OF "HSV" WHICH CAN BE CHANGED DYNAMICALLY SO AS TO DETECT THE DESIRED COLOUR
lh = cv.createTrackbar("LH","Tracking",0,255,nothing)
ls = cv.createTrackbar("LS","Tracking",0,255,nothing)
lv = cv.createTrackbar("LV","Tracking",0,255,nothing)
uh = cv.createTrackbar("UH","Tracking",255,255,nothing)
us = cv.createTrackbar("US","Tracking",255,255,nothing)
uv = cv.createTrackbar("UV","Tracking",255,255,nothing)

cap=cv.VideoCapture(0)

while(1):
    check,frame=cap.read()  # READING FRAMES FROM THE WEBCAM
    hsv= cv.cvtColor(frame, cv.COLOR_BGR2HSV) # CONVERTING BGR TO HSV
    cv.imshow("Balls",frame)
    cv.imshow("HSV",hsv)
    l_h=cv.getTrackbarPos("LH","Tracking")
    l_s=cv.getTrackbarPos("LS","Tracking")
    l_v=cv.getTrackbarPos("LV","Tracking")

    u_h=cv.getTrackbarPos("LH","Tracking")
    u_s=cv.getTrackbarPos("US","Tracking")
    u_v=cv.getTrackbarPos("UV","Tracking")

    lb=np.array([l_h,l_s,l_v],np.uint8)  # CREATING NUMPY ARRAY OF THE LOWER BOUND HSV VALUES
    ub=np.array([u_h,u_s,u_v],np.uint8)  # CREATING NUMPY ARRAY OF THE LOWER UPPER HSV VALUES
    mask = cv.inRange(hsv,lb,ub)         # CREATING A MASK

    cv.imshow("MASK",mask)
    result= cv.bitwise_and(frame,frame,mask=mask)  #
    cv.imshow("RESULT",result)
    if cv.waitKey(1)==27:
        break

cv.destroyAllWindows()