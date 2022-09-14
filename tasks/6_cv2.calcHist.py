# importing required libraries of opencv
import cv2

# importing library for plotting
from matplotlib import pyplot as plt

# reads an input image
img = cv2.imread('source/imput1.jpeg',0)

# find frequency of pixels in range 0-255
histr = cv2.calcHist([img],[0],None,[256],[0,256])

# show the plotting graph of an image
img = cv2.resize(img,dsize=[0,0],fx=0.2,fy=0.2,)
cv2.imshow('image',img)
cv2.waitKey(0)
plt.plot(histr)
plt.show()


#####  image to histogram  #####