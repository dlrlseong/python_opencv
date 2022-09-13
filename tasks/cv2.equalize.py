import cv2
import numpy as np

img = cv2.imread('/Users/dlrlseong/python/test.jpg', 0)
img = cv2.resize(img, dsize=(0, 0), fx=3, fy=3)
cv2.imshow('1',img)

equalizeHist = cv2.equalizeHist(img)

cv2.imshow('2',equalizeHist)
cv2.waitKey(0)