import cv2

image = cv2.imread('/Users/dlrlseong/python/rgb.png')
B, G, R = cv2.split(image)
# Corresponding channels are separated

cv2.imshow("original", image)


cv2.imshow("blue", B)


cv2.imshow("Green", G)


cv2.imshow("red", R)

cv2.waitKey(0)
cv2.destroyAllWindows()
