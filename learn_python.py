# if statement 
num =0
'''

if num <4 :
    print('short')
elif num ==3:
    print('equality')
else:   
    print('long')
print('hello wolrd')

genre =['oussama','hacen','jack','katie']
#for i in range(len(genre)):
 #   print(genre[i])
for i in genre:
    print(i)
else :
    print('no element')

while num <10 :

    print(num)
    num +=1
else :
    print('end process')    


class Student :
    def __init__(self,name, marks):
        self.name=name
        self.marks=marks
        
    def chek_padd_fail(self):
        if self.marks >40 :
            return True
        else :
            return False    
student1=Student('oussama',23)
print(student1.name)
print(student1.marks)

class Com_Number:
    def __init__(self,imaginary,reel):
        self.imaginary=imaginary
        self.reel=reel
    def get_complexeNumber(self):
        return self.imaginary,'i' ,' + ', self.reel
        

firstnumber =Com_Number(2,4)
print(firstnumber.get_complexeNumber())
'''
""" class Polygon :
    def __init__(self,sides):
        self.sides=sides
    def display_info(self):
        print('a polygon its two dimensional shape with straight lines')
    def get_primeter(self):
        primeter=sum(self.sides)
        return primeter
class Triangle(Polygon):
    def display_info(self):
        print('a triangle is a polygon with 3 edges')

class Quadrilateral(Polygon):
    def display_info(self):
        print('a Quadrilateral is a polygon with 4 edges')

t1=Triangle([2,3,4])

t1.display_info() """
""" class Point ():
    def __init__ (self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return '({0},{1})'.format(self.x,self.y)
    def __add__ (self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Point(x,y)
p1=Point(2,3)
p2=Point(4,5)
print(p1+p2) """
""" import cv2

img = cv2.imread('./image.jpeg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, binaryImg = cv2.threshold(grayImg, 0, 255, cv2.THRESH_OTSU)

cv2.imshow('RGB image', img)
cv2.imshow('Binary image', binaryImg)
cv2.waitKey(0)
cv2.destroyAllWindows() """

import cv2
import numpy as np
img = cv2.imread('bict 2.jpeg',0)
img2 = cv2.imread('bict 2.jpeg',1)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
hist_norm = hist.ravel()/hist.max()
Q = hist_norm.cumsum()
bins = np.arange(256)
fn_min = np.inf
thresh = -1
for i in range(1,256):
    p1,p2 = np.hsplit(hist_norm,[i]) 
    q1,q2 = Q[i],Q[255]-Q[i] 
    if q1 == 0:
        q1 = 0.00000001
    if q2 == 0:
        q2 = 0.00000001
b1,b2 = np.hsplit(bins,[i]) 
m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
fn = v1*q1 + v2*q2
if fn < fn_min:
    fn_min = fn
    thresh = i
ret, otsu = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print (thresh,ret)
(thresh,Bin)=cv2.threshold(img,ret,255,cv2.THRESH_BINARY)
cv2.imshow('orignal',img2)
cv2.imshow('binary',Bin)
cv2.waitKey(0)