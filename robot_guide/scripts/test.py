#!/usr/bin/env python
import cv2
import numpy as np
import pandas as pd
import rospy
from pyzbar import pyzbar
from std_msgs.msg import String
from geometry_msgs.msg import Twist

video_capture = cv2.VideoCapture(0) 

# variable
vel_msg = Twist()
vel_msg.linear.x = 0    
vel_msg.linear.y = 0
vel_msg.linear.z = 0
vel_msg.angular.x = 0
vel_msg.angular.y = 0
vel_msg.angular.z = 0

# give to the robot directions to look at 
# to center the qr code
def where_to_look(shape_x,shape_y,middle_x,middle_y):
    global vel_msg
    center_x = shape_x / 2
    center_y = shape_y / 2
    threshold_x = shape_x * 0.05
    threshold_y = shape_y * 0.05

    if middle_x < (center_x - threshold_x) or middle_x > (center_x + threshold_x):
        print("middle_x:",middle_x)
        print("center_x:",center_x)
        if middle_x < (center_x):
            print("Turn left")
            vel_msg.angular.x = -0.5

        else:
            print("Turn right")
            vel_msg.angular.x = +0.5

        have_to_move_x = True
    else:
        print ("Perfectly accurate x!")
        have_to_move_x= False
    
    if middle_y < (center_y - threshold_y) or middle_y > (center_y + threshold_y):
        print("middle_y:",middle_y)
        print("center_y:",center_y)
        if middle_y < (center_y):
            print("Look up")
            pass
        else:
            print("Look down")
            pass
    
        have_to_move_y = True

    else: 
        print("Perfectly accurate y!")
        have_to_move_y = False

    if have_to_move_x == False :
        vel_msg.linear.x = 0.5

# main
def main():
    
    ret, frame = video_capture.read()
    
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

def move():
    rospy.init_node('qr_code_follow', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    global vel_msg

    while not rospy.is_shutdown():

        vel_msg.linear.x = 0    
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

        main()

        velocity_publisher.publish(vel_msg)


    vel_msg.linear.x = 0
    vel_msg.angular.x = 0
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass

video_capture.release() 
cv2.destroyAllWindows() 