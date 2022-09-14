import cv2
import numpy as np

FILE_NAME = 'source/test.jpg'
# Create translation matrix.
# If the shift is (x, y) then matrix would be
# M = [1 0 x]
#	 [0 1 y]
# Let's shift by (100, 50).
M = np.float32([[1, 0, 100], [0, 1, 50]])

try:

    # Read image from disk.
    img = cv2.imread(FILE_NAME)
    (rows, cols) = img.shape[:2]

    # warpAffine does appropriate shifting given the
    # translation matrix.
    res = cv2.warpAffine(img, M, (cols, rows))

    # Write image back to disk.
    # cv2.imwrite('result.jpg', res)
    cv2.imshow('result',res)
    cv2.imshow('original',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except IOError:
	print ('Error while reading files !!!')
