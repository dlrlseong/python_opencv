# Python program to illustrate
# arithmetic operation of
# addition of two images

# organizing imports
import cv2
import numpy as np

# path to input images are specified and
# images are loaded with imread command
image1 = cv2.imread('source/imput1.jpeg')
image2 = cv2.imread('source/input2.jpeg')

# cv2.addWeighted is applied over the
# image inputs with applied parameters
sum = cv2.add(image1, image2)
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)

# the window showing output image
# with the weighted sum
cv2.imshow('Weighted Image', weightedSum)
cv2.imshow('sum',sum)

cv2.imshow('image1', image1)
cv2.imshow('image2', image2)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
