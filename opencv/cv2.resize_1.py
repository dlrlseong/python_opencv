import cv2
import numpy as np

FILE_NAME = 'C:\openCV\sample_image.png'

# Read image from disk.
img = cv2.imread(FILE_NAME)
print(img.shape)
# Get number of pixel horizontally and vertically.
(height, width) = img.shape[:2]
print((height, width))


# Specify the size of image along with interploation methods.
# cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC
# is used for zooming.
res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)
print(res.shape)
# Write image back to disk.
cv2.imwrite('result.jpg', res)

cv2.imshow('1',res)
cv2.waitKey(0)


