#!/usr/bin/python
import cv2
import numpy as np

#Now define the boundaries for the colors that we want to capture
boundaries = [
 ([0, 0, 0], [255,50, 50]), #blue
 ([0, 0, 0], [50,255, 50]), #green
 ([0, 0, 0], [50,50, 255]), #red
]

def start(image):
    for (lower, upper) in boundaries:
    	lower = np.array(lower, dtype = "uint8")
    	upper = np.array(upper, dtype = "uint8")
    	mask = cv2.inRange(image, lower, upper)
    	output = cv2.bitwise_and(image, image, mask = mask)
    	cv2.imshow("images", np.hstack([image, output]))
    	cv2.waitKey(0)
