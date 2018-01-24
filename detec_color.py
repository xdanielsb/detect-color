#!/usr/bin/python
import argparse
import cv2
from logic import start

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

if __name__ == "__main__":
    start(image)
