# Python program to explain cv2.erode() method

# importing cv2
import cv2

# importing numpy
import numpy as np

# path
path = r'source/test.jpg'

# Reading an image in default mode
image = cv2.imread(path)

original = image

# Window name in which image is displayed
window_name = 'Image'

# Creating kernel
kernel_5x5 = np.ones((5, 5), np.uint8)
kernel_2x2 = np.ones((2, 2), np.uint8)
kernel_10x10 = np.ones((10, 10), np.uint8)

# Using cv2.erode() method
image_5x5 = cv2.erode(image, kernel_5x5)
image_2x2 = cv2.erode(image, kernel_2x2)
image_10x10 = cv2.erode(image, kernel_10x10)

# Displaying the image
cv2.imshow('kernel 2x2', image_2x2)
cv2.imshow('kernel 5x5', image_5x5)
cv2.imshow('kernel 10x10', image_10x10)
cv2.imshow('Original', original)

cv2.waitKey(0)
