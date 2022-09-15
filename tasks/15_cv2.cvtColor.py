# Python program to read image as RGB

# Importing cv2 and matplotlib module
import cv2
import matplotlib.pyplot as plt

# reads image as RGB
# shows the image
img = cv2.imread('source/gfg.png')
cv2.imshow('Original',img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('BGR2HSV',img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('BGR2LAB',img)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('EdgeMap', laplacian)



cv2.waitKey(0)
cv2.destroyAllWindows()
