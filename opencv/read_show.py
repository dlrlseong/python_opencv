import cv2

img = cv2.imread('/Users/dlrlseong/python/test.jpg', cv2.IMREAD_GRAYSCALE)
# img = img/255
print(img)
print(img.shape)
print(type(img))
print(img.dtype)
cv2.imshow('1', img)
cv2.waitKey(0)
# TODO: Check Erosion
# cv2.imwrite('img_gray.jpg',img)
