import sys
import cv2
import numpy as np

'''
Takes in two image file names as arguments.
Compares the two given files and states whether they are equal or not.
'''


def image_compare():
    if first_image.shape == second_image.shape:
        diff = cv2.subtract(first_image, second_image)

        b, g, r = cv2.split(diff)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("Images are completely equal")
        else:
            print("Images are NOT equal")

    else:
        print("Images are NOT equal")


if len(sys.argv) == 3:
    first_image = cv2.imread(sys.argv[1])
    second_image = cv2.imread(sys.argv[2])
    image_compare()
else:
    print("Missing arguments: <first_file> <second_file>")