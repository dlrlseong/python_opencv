import cv2

# Read the image.
img = cv2.imread('source/noisy.jpg')
# img = cv2.resize(img, (0, 0), fx=2, fy=2)

cv2.imshow('Original',img)
# Apply bilateral filter with d = 15,
# sigmaColor = sigmaSpace = 75.
bilateral = cv2.bilateralFilter(img, 15, 75, 75)

# Save the output.
cv2.imshow('taj_bilateral.jpg', bilateral)


img = cv2.blur(img, (5, 5))
cv2.imshow('blur',img)

img = cv2.medianBlur(img, 5)
cv2.imshow('median',img)

img = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow('GaussianBlur',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
