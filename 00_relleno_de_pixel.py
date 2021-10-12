import cv2
import numpy as np

img= np.zeros((400,500),np.uint8)
img[200,:]= 100

# La función floodfill recibe la imagen en la que se trabajará, una máscara que
# en nuestro caso será None, la posición x,y donde comienza el algoritmo y el color
cv2.floodFill(img, None, (80, 300), 255)
cv2.imshow('imagen', img)
cv2.waitKey()