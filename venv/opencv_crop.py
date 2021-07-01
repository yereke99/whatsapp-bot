import cv2
import numpy as np

image = cv2.imread('out0.jpg')

crop = image[1558:3000, 200:1995]


cv2.imshow('crop', crop)
cv2.waitKey(0)