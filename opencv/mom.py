import cv2


img_grayScale = cv2.imread('/Users/dlrlseong/python/test.jpg', 0)
img_color = cv2.imread('/Users/dlrlseong/python/test.jpg', 1)

try:
    # Read image from disk.
    img = cv2.imread('/Users/dlrlseong/python/test.jpg', 1)

    # Canny edge detection.
    edges = cv2.Canny(img, 100, 200)

    # Write image back to disk.
    cv2.imshow('edges',edges)
    cv2.waitKey(0)
    #cv2.imwrite('result.jpg', edges)
except IOError:
	print ('Error while reading files !!!')


cv2.imshow('color',img_color)
cv2.imshow('gray',img_grayScale)
cv2.waitKey(0)