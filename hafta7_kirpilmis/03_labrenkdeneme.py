import cv2

img = cv2.imread("labrenk.jpg")

print(img.shape)

color1point = img[50,100]
print(color1point)

# 0 blue
# 1 green
# 2  red

Blue = color1point[0]
print(Blue)

cv2.imshow("deneme rengi", img)



cv2.waitKey(0)
cv2.destroyAllWindows()
