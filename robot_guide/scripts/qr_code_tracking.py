import cv2
import numpy as np
import pandas as pd
import rospy
from pyzbar import pyzbar

video_capture = cv2.VideoCapture(0) 

# give to the robot directions to look at 
# to center the qr code
def where_to_look(shape_x,shape_y,middle_x,middle_y):

    center_x = shape_x / 2
    center_y = shape_y / 2
    threshold_x = shape_x * 0.05
    threshold_y = shape_y * 0.05

    if middle_x < (center_x - threshold_x) or middle_x > (center_x + threshold_x):
        print("middle_x:",middle_x)
        print("center_x:",center_x)
        if middle_x < (center_x):
            print("Turn left")
            pass

        else:
            print("Turn right")
            pass
        pass
    else:
        print ("Perfectly accurate x!")
        pass
    
    if middle_y < (center_y - threshold_y) or middle_y > (center_y + threshold_y):
        print("middle_y:",middle_y)
        print("center_y:",center_y)
        if middle_y < (center_y):
            print("Look up")
            pass
        else:
            print("Look down")
            pass
    else: 
        print("Perfectly accurate y!")
        pass

# main
while(True):

    ret, frame = video_capture.read()
    if not ret:
        break
    (shape_y,shape_x, osef) = frame.shape

    # insert code here

    qrcodes = pyzbar.decode(frame)

    for qrcode in qrcodes :
        qrcodeData = qrcode.data.decode("utf-8")
        if qrcodeData == "Follow me!" :
            (x, y, w, h) = qrcode.rect
            middle_x = x +(w/2)
            middle_y = y + (h/2)
            where_to_look(shape_x,shape_y,middle_x,middle_y)

    # end of code 

    # display 
    cv2.imshow('Video', frame)

    # if you press 'q' it will exit the programm
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release() 
cv2.destroyAllWindows() 