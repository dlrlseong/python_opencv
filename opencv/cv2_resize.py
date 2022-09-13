import cv2

img = cv2.imread('C:\openCV\sample_image.png')

half = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
cv2.imshow('Original', img)
cv2.imshow('half', half)


cv2.waitKey(0)


