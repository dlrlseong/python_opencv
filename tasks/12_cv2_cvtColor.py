# Python program to explain cv2.cvtColor() method

# importing cv2
import cv2

# path
path = r'source/test.jpg'

# Reading an image in default mode
src = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Using cv2.cvtColor() method
# Using cv2.COLOR_BGR2GRAY color space
# conversion code
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# Displaying the image
cv2.imshow('src', src)
cv2.imshow('BGR2GRAY', image)

test_image = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
cv2.imshow('BGR2RGB', test_image)

img3 = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
cv2.imshow('BGR2HSV', img3)

cv2.waitKey(0)
