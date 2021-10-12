import cv2

img = cv2.imread('autopista.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask_i = cv2.inRange(hsv,(0,0,60),(180,45,185))

mask = cv2.bitwise_not(mask_i)
img_2 = cv2.bitwise_and(img, img, mask=mask)

#cv2.imshow('Imagen original',img)
cv2.imshow('Imagen', img_2)
cv2.waitKey(0)