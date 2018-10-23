import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:\\Users\\Admin\\Desktop\\opencv\\watch1.jpg',cv2.IMREAD_GRAYSCALE)
#BGRA - Blue green red alpha, Alpha is only one color
#IMREAD_COLOR - 1 - color , 0 - grayscale
#IMREAD_UNCHANGED = -1

#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.circle([50,100],[80,100],color='r',linewidth=5)
plt.show()
