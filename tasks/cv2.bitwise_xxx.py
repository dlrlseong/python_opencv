# Python program to illustrate
# arithmetic operation of
# bitwise AND of two images

# organizing imports
import cv2
import numpy as np

# path to input images are specified and
# images are loaded with imread command
img1 = cv2.imread('/Users/dlrlseong/python/bitwise1.png')
img2 = cv2.imread('/Users/dlrlseong/python/bitwise2.png')

# cv2.bitwise_and is applied over the
# image inputs with applied parameters
dest_and = cv2.bitwise_and(img2, img1, mask=None)
dest_or = cv2.bitwise_or(img2, img1, mask=None)
dest_xor = cv2.bitwise_xor(img2, img1, mask=None)
dest_not1 = cv2.bitwise_not(img1, mask=None)
dest_not2 = cv2.bitwise_not(img2, mask=None)

# the window showing output image
# with the Bitwise AND operation
# on the input images
cv2.imshow('Bitwise1', img1)
cv2.imshow('Bitwise2', img2)
cv2.imshow('Bitwise And', dest_and)
cv2.imshow('Bitwise Or', dest_or)
cv2.imshow('Bitwise Xor', dest_xor)
cv2.imshow('Bitwise not1', dest_not1)
# cv2.imshow('Bitwise not2', dest_not2)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
