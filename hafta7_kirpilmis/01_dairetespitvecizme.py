# 10 CM
# sadece daireyi tespit edip, çizme kodu
import cv2
import numpy as np 

img = cv2.imread("2ornek_15_10cm.jpg")
height = img.shape[0]
width = img.shape[1]
newheight =int(height*0.8)
newwidth = int(width*0.8)

img = cv2.resize(img, (newwidth,newheight))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)
# daire algılama işi:
# ilk gelen örnekler için çalışan parametreler:
#  circle = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,dp=1,minDist=700,param1=150,param2=30,minRadius=100,maxRadius=800)
circle = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,dp=1,minDist=700,param1=200,param2=30,minRadius=100,maxRadius=800)


#algılanan daireyi çizme:
if circle is not None:
    # around ile daire degerleri yuvarlandı, uint ile tamsayıya dönüştürüldü
    # circle parametreleri x ve y: dairenin merkez koordinatları, r: yarıçapı
    circle = np.uint16(np.around(circle))
    for (x,y,r) in circle[0,]:
        # r piksel yarıçapı büyüklüğünde daire çiz
        cv2.circle(img, (x,y), r, (0,255,0),10)
        # 3 piksel yarıçapında çiz (merkez koordinattan)
        cv2.circle(img,(x,y), 3 , (0,0,255),2)
     


cv2.imshow("ornek1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()