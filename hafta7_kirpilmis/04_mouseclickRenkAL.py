import cv2 
import numpy as np

img = cv2.imread("2ornek_1_10cm.jpg")
height = img.shape[0]
width = img.shape[1]
newheight =int(height*0.6)
newwidth = int(width*0.6)

img = cv2.resize(img, (newwidth,newheight))

# 0 blue
# 1 green
# 2  red


def fare_tiklama(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        renk_degeri = img[y, x]  # Tıklanan pikselin BGR renk değerini al
        print("Tıklanan noktanın renk değeri (BGR formatında):", renk_degeri)

cv2.imshow("mouseilen",img)
cv2.setMouseCallback("mouseilen",fare_tiklama)

cv2.waitKey(0)
cv2.destroyAllWindows()