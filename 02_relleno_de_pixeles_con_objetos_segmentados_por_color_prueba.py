import cv2
import numpy as np

img = cv2.imread('autopista.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask_i = cv2.inRange(hsv,(0,0,60),(180,45,185))
mask = cv2.bitwise_not(mask_i)

mask_inv = cv2.bitwise_not(mask)
img_fl = mask_inv.copy()
h, w = mask_inv.shape
mask_hw = np.zeros((h+2, w+2),np.uint8)
cv2.floodFill(img_fl, mask_hw, (1, 1), 255)
img_fl_inv = cv2.bitwise_not(img_fl)

fill_img = cv2.bitwise_or(mask_inv, img_fl_inv)

cv2.imshow('Paso 1: Imagen original', mask_i)
cv2.imshow('Paso 2: Imagen floodFill', img_fl)
cv2.imshow('Paso 3: Imagen negativa', img_fl_inv)
cv2.imshow('Paso 4: Imagen sin huecos', fill_img)
cv2.waitKey(0)