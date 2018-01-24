#!/usr/bin/python
import cv2
import numpy as np
import argparse

__author__ = "Daniel Fernando Santos Bustos"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Daniel Santos"
__email__ = "dfsantosbu@unal.edu.co"
__status__ = "Production"

#Create a parser
arguments_parser = argparse.ArgumentParser()
arguments_parser.add_argument("-i", "--image", help= "path to the image")
arguments  = vars(arguments_parser.parse_args())

#load the image
image = cv2.imread(arguments["image"])

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

if __name__ == "__main__":
    start(image)
