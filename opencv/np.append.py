import cv2
import numpy as np

img1 = cv2.imread('/Users/dlrlseong/python/img.png')
img2 = cv2.imread('/Users/dlrlseong/python/img2.png')
resize1 = cv2.resize(img1, (205, 145), interpolation=cv2.INTER_LINEAR)
resize2 = cv2.resize(img2, (205, 339), interpolation=cv2.INTER_NEAREST)

print(resize1.shape)
print(resize2.shape)



new = np.append(resize1, resize2, axis=0)
# print(new.shape)
cv2.imwrite('image.png',new)
cv2.imshow('1',new)
cv2.waitKey(0)
