#!/usr/bin/env python
import cv2
import numpy as np
import pandas as pd
import rospy
from pyzbar import pyzbar
from std_msgs.msg import String
from geometry_msgs.msg import Twist

video_capture = cv2.VideoCapture(6)

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
def where_to_look(shape_x,middle_x):
    global vel_msg
    center_x = shape_x / 2
    threshold_x = shape_x * 0.05

    if middle_x < (center_x - threshold_x) or middle_x > (center_x + threshold_x):
        if middle_x < (center_x):
            vel_msg.linear.x = 0.2
            vel_msg.angular.z = -0.5
        else:
            vel_msg.linear.x = 0.2
            vel_msg.angular.z = +0.5
    else:
        vel_msg.linear.x = 0.2

# main
def main():
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0

    ret, frame = video_capture.read()
    
    (shape_y,shape_x, osef) = frame.shape

    # insert code here

    qrcodes = pyzbar.decode(frame)
    if(qrcodes):
        for qrcode in qrcodes :
            qrcodeData = qrcode.data.decode("utf-8")
            if qrcodeData == "Follow me!" :
                (x, y, w, h) = qrcode.rect
                middle_x = x +(w/2)
                where_to_look(shape_x,middle_x)
    else:
        vel_msg.linear.x = 0
        vel_msg.angular.x = 0
    # end of code 

    # display 
    cv2.imshow('Video', frame)

def move():
    rospy.init_node('qr_code_follow', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
    global vel_msg

    while not rospy.is_shutdown():
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

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
