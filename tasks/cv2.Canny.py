import cv2
import numpy as np

FILE_NAME = '/Users/dlrlseong/python/test.jpg'
try:
    # Read image from disk.
    img = cv2.imread(FILE_NAME)

    # Canny edge detection.
    edges = cv2.Canny(img, 100, 200)

    # Write image back to disk.
    cv2.imshow('edges',edges)
    cv2.waitKey(0)
    #cv2.imwrite('result.jpg', edges)
except IOError:
	print ('Error while reading files !!!')



    ######  edge detection  ######
