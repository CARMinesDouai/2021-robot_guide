#!/usr/bin/env python
import cv2
import numpy as np
import pandas as pd
import rospy

video_capture = cv2.VideoCapture(0) 
detector = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel") 


while(True):

    ret, frame = video_capture.read()
    if not ret:
        break

    base_frame = frame.copy()
    
    original_size = frame.shape
    target_size = (300, 300)
    resized_frame = cv2.resize(frame, target_size)
    
    aspect_ratio_x = (original_size[1] / target_size[1])
    aspect_ratio_y = (original_size[0] / target_size[0])

    imageBlob = cv2.dnn.blobFromImage(image = resized_frame)
    detector.setInput(imageBlob)
    detections = detector.forward() 

    detections_df = pd.DataFrame(detections[0][0]
    , columns = ["img_id", "is_face", "confidence", "left", "top", "right", "bottom"])

    detections_df = detections_df[detections_df['is_face'] == 1] #0: background, 1: face
    detections_df = detections_df[detections_df['confidence'] >= 0.520]
    donnees = {}
    for i, instance in detections_df.iterrows():
        
        confidence_score = str(round(100*instance["confidence"], 2))+" %"
        
        left = int(instance["left"] * 300)
        bottom = int(instance["bottom"] * 300)
        right = int(instance["right"] * 300)
        top = int(instance["top"] * 300)
            
        detected_face = base_frame[int(top*aspect_ratio_y):int(bottom*aspect_ratio_y), int(left*aspect_ratio_x):int(right*aspect_ratio_x)]
        
        if detected_face.shape[0] > 0 and detected_face.shape[1] > 0:
            
            left = int(left*aspect_ratio_x)
            top = int(top*aspect_ratio_y)
            right = int(right*aspect_ratio_x)
            bottom = int(bottom*aspect_ratio_y)

            #write the confidence score above the face
            cv2.putText(base_frame, confidence_score, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            #draw rectangle to main image
            cv2.rectangle(base_frame, (left, top), (right, bottom), (255, 255, 255), 1) 
            
            for variable in ["confidence_score", "left", "top", "right", "bottom"]:
                donnees[variable] = eval(variable)

    cv2.imshow('Video', base_frame)
    # if you press 'q' it will exit the programm
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
video_capture.release() 
cv2.destroyAllWindows() 
