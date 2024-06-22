import cv2
import numpy as np
from colour.models import RGB_to_XYZ, XYZ_to_Lab
from skimage import color
import sqlite3 as sql
import pandas as pd

conn = sql.connect('veriTabani3.db')
cursor = conn.cursor()

img = cv2.imread("ornek_1_10cm.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circle = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1,minDist=20,param1=50,param2=30,minRadius=10,maxRadius=100)

if circle is not None:
    circle = np.uint16(np.around(circle))
    for (x,y,r) in circle[0, ]:
        # Dairenin koordinatlarını yeniden boyutlandır
        x_resized = int(x * 600 / img.shape[1]) # Yeni genişlik: 600
        y_resized = int(y * 800 / img.shape[0]) # Yeni yükseklik: 800
        r_resized = int(r * 600 / img.shape[1]) # Yeni genişlik: 600
        cv2.circle(img, (x_resized, y_resized), r_resized, (0,255,0), 2)
        cv2.circle(img, (x_resized, y_resized), 3, (0,255,0), 2)
        print(f'Merkez Koordinatları: ({x_resized},{y_resized})')
        colorsB = img[y,x,0]
        colorsG = img[y,x,1]
        colorsR = img[y,x,2]
        colors1 = img[y,x]
        colors2 = img[y-40,x]
        colors3 = img[y-30,x]
        colors4 = img[y+30,x]
        colors5 = img[y+40,x]
        colors6 = img[y,x-40]
        colors7 = img[y,x-30]
        colors8 = img[y,x+30]
        colors9 = img[y,x+40]

all_colorsB = []
all_colorsG = []
all_colorsR = []

all_colorsB.extend([colors1[0], colors2[0], colors3[0], colors4[0], colors5[0], colors6[0], colors7[0], colors8[0], colors9[0]])
all_colorsG.extend([colors1[1], colors2[1], colors3[1], colors4[1], colors5[1], colors6[1], colors7[1], colors8[1], colors9[1]])
all_colorsR.extend([colors1[2], colors2[2], colors3[2], colors4[2], colors5[2], colors6[2], colors7[2], colors8[2], colors9[2]])

averageB = sum(all_colorsB) / len(all_colorsB)
averageG = sum(all_colorsG) / len(all_colorsG)
averageR = sum(all_colorsR) / len(all_colorsR)

print("Blue Average:", averageB)
print("Green Average:", averageG)
print("Red Average:", averageR)

B = averageB / 255
R = averageR / 255
G = averageG / 255

RGB = np.array([R, G, B])

Lab = color.rgb2lab([[RGB]])

L = Lab[0][0][0]
a = Lab[0][0][1]
b = Lab[0][0][2]

print("CIE LAB L*: ", L)
print("CIE LAB a*: ", a)
print("CIE LAB b*: ", b)

cursor.execute('''CREATE TABLE IF NOT EXISTS LabData (id INTEGER PRIMARY KEY, L REAL, a REAL, b REAL)''')
cursor.execute('''INSERT INTO LabData (L, a, b) VALUES (?, ?, ?)''', (L, a, b))

df = pd.read_sql_query("SELECT * FROM LabData;", conn)

df.to_excel('LabData2.xlsx', index=False)

conn.commit()
conn.close()

cv2.namedWindow("Daire Tespiti", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Daire Tespiti", 600, 800)

cv2.imshow("Daire Tespiti", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
