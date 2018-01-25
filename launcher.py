#!/usr/bin/python
import argparse
import cv2
import os
from src.logic import start

__author__ = "Daniel Fernando Santos Bustos"
__license__ = "GPL V3"
__version__ = "1.0"
__maintainer__ = "Daniel Santos"
__email__ = "dfsantosbu@unal.edu.co"
__status__ = "Production"


if __name__ == "__main__":
    #Create a parser
    arguments_parser = argparse.ArgumentParser()
    arguments_parser.add_argument("-i", "--image", help= "path to the image")
    arguments  = vars(arguments_parser.parse_args())

    if arguments["image"] == None:
        print("\nHello User!\nUser for using the software you must compile the software in this way:\n\n\t python launcher.py --image path_to_image")
        print("anyway We are going to show a simple example.")
        #load the image
        image = cv2.imread("img/test.png")
        start(image)
    else:
        #load the image
        if(os.path.exists(arguments["image"])):
            image = cv2.imread(arguments["image"])
            start(image)
        else:
            print("User the file image {} not exist.".format(arguments["image"]))
