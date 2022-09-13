# importing libraries
import cv2
import numpy as np

image = cv2.imread('C:\openCV\sample_image.png')

cv2.imshow('Original Image', image)


# Gaussian Blur
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)


# Median Blur
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)


# Bilateral Blur
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
