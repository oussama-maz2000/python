import cv2
import numpy as np
image=cv2.imread('bact.jpeg')
image=cv2.resize(image,(800,600))
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('img2',gray_image) 
#cv2.waitKey(0) 
hist=cv2.calcHist([gray_image],[0],None,[255],[0,255])
within=[]
for i in range(len(hist)):
    x,y=np.split(hist,[i])
    x1=np.sum(x)/(image.shape[0]*image.shape[1])
    y1=np.sum(y)/(image.shape[0]*image.shape[1])
    x2=np.sum([j*t for j,t in enumerate(x)]/np.sum(x))
    y2=np.sum([j*t for j,t in enumerate(y)]/np.sum(y))
    x3=np.sum([(j-x2)**2*t for j,t in enumerate(x)])/np.sum(x)
    x3 =np.nan_to_num(x3)
    y3=np.sum([(j-y2)**2*t for j,t in enumerate(y)])/np.sum(y)
    within.append(x1*x3+y1*y3)
m=np.argmax(within)
print(m)
(thresh,Bin)=cv2.threshold(gray_image,m,255,cv2.THRESH_BINARY)
cv2.imshow('binary',Bin)
cv2.waitKey(0) 

