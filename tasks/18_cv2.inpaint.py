import numpy as np
import cv2

# Open the image.
img = cv2.imread('source/cat_damaged.png')
img = cv2.resize(img, (0, 0), fx=0.7, fy=0.7)

# Load the mask.
mask = cv2.imread('source/cat_mask.png', 0)
mask = cv2.resize(mask, (0, 0), fx=0.7, fy=0.7)

# Inpaint.
dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

# Write the output.

cv2.imshow('Original',img)
cv2.imshow('Mask',mask)
cv2.imshow('cat_inpainted.png', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
