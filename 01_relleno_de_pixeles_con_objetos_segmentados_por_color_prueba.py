import cv2
import numpy as np

img = cv2.imread('imagen.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask_orange = cv2.inRange(hsv,(3,153,175),(10,220,245))
mask = cv2.bitwise_not(mask_orange)

mask_inv = cv2.bitwise_not(mask)
img_fl = mask_inv.copy()
h, w = mask_inv.shape
mask_hw = np.zeros((h+2, w+2),np.uint8)
cv2.floodFill(img_fl, mask_hw, (1, 1), 255)
img_fl_inv = cv2.bitwise_not(img_fl)

fill_img = cv2.bitwise_or(mask_inv, img_fl_inv)

cv2.imshow('Paso 0: Imagen original', mask_orange)
cv2.imshow('Paso 1: Imagen floodFill', img_fl)
cv2.imshow('Paso 2: Imagen negativa', img_fl_inv)
cv2.imshow('Paso 3: Imagen sin huecos', fill_img)
cv2.waitKey(0)