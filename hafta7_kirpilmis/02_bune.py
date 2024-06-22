# 10 - 15 - 20 CM İÇİN ÇALIŞAN KOD
# sadece daireyi tespit edip, çizme kodu

# NE OLURSA OLSUN *UYGUN* CIE LAB DEGERİ ÇIKMIYO

import cv2
import numpy as np 
from skimage import color

img = cv2.imread("2ornek_1_25cm.jpg")
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
        print(f'Merkez Koordinatları: ({x},{y})')
        #fotografın orta koordinattaki b,g,r degerlerini alma:
        colorsB = img[y,x,0] # x,y deki blue degeri
        colorsG = img[y,x,1]
        colorsR = img[y,x,2]
        colors1 = img[y,x]  #--> x,y'deki BGR degerini (b,g,r) şeklinde döndürecek
        # x,y nin aşağı ve yukarısından
        colors1 = img[y, x]
        colors2 = img[y - 40, x]
        colors3 = img[y - 30, x]
        colors4 = img[y + 30, x]
        colors5 = img[y + 40, x]
        colors6 = img[y, x - 40]
        colors7 = img[y, x - 30]
        colors8 = img[y, x + 30]
        colors9 = img[y, x + 40]
        colors10 = img[y - 20, x - 20]
        colors11 = img[y - 20, x + 20]
        colors12 = img[y + 20, x - 20]
        colors13 = img[y + 20, x + 20]
        colors14 = img[y - 10, x - 10]
        colors15 = img[y - 10, x + 10]
        colors16 = img[y + 10, x - 10]
        colors17 = img[y + 10, x + 10]



        


# ilgili piksellerin renk degerlerini içerecek boş listeler oluştur:
all_colorsB = []        
all_colorsG = []
all_colorsR = []

# her pikselin, sırayla b,g,r degerlerini tek dizide topla:
all_colorsB.extend([colors1[0],colors2[0],colors3[0],colors4[0],
                    colors5[0],colors4[0],colors5[0],colors6[0],
                    colors7[0],colors8[0],colors9[0],colors10[0],
                    colors11[0],colors12[0],colors13[0],colors14[0],
                    colors14[0],colors15[0],colors16[0],colors17[0]])

all_colorsG.extend([colors1[1], colors2[1], colors3[1], colors4[1], colors5[1],
                    colors4[1], colors5[1], colors6[1], colors7[1], colors8[1],
                    colors9[1], colors10[1], colors11[1], colors12[1], colors13[1],
                    colors14[1], colors14[1], colors15[1], colors16[1], colors17[1]])

all_colorsR.extend([colors1[2], colors2[2], colors3[2], colors4[2], colors5[2],
                    colors4[2], colors5[2], colors6[2], colors7[2], colors8[2],
                    colors9[2], colors10[2], colors11[2], colors12[2], colors13[2],
                    colors14[2], colors14[2], colors15[2], colors16[2], colors17[2]])

# len, dizi içinde kaç eleman oldugunu verir
# renk degerlerinin ortalamalarını hesaplayalım:
averageB = sum(all_colorsB)/len(all_colorsB)
averageG = sum(all_colorsG)/len(all_colorsG)
averageR = sum(all_colorsR)/len(all_colorsR)

# CIE LAB formatına çevirmek için gerekli ortalama BGR degerlerimiz:
print("Blue Average:", averageB)
print("Green Average:", averageG)
print("Red Average:", averageR)

# RGB değerlerini 0-1 aralığına normalize et
# CIE LAB dönüştürme için gerekli parametre ???????????????
B = averageB / 255
R = averageR / 255
G = averageG / 255

# BGR'den XYZ'ye dönüşüm için RGB dizisini oluştur
RGB = np.array([R, G, B])

# RGB'den CIE LAB'ye dönüşümü gerçekleştirin
#buradaki iki köşeli parantezin gerekliliği(????)
Lab = color.rgb2lab([[RGB]])

# CIE LAB formatında L, a, b degerlerini al
L = Lab[0][0][0]
a = Lab[0][0][1]
b = Lab[0][0][2]

# CIE LAB formatında L*, a* ve b* değerlerini yazdırın
print("CIE LAB L*: ", L)
print("CIE LAB a*: ", a)
print("CIE LAB b*: ", b)


cv2.imshow("ornek1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()