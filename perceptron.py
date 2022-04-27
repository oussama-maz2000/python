from matplotlib import pyplot as plt
import numpy as np

x3=np.random.random_integers(7,size=(4,2))
data_set=np.array([[0.325,0.768,1],[0.798,0.821,1],[0.364,0.417,1],[0.241,0.605,1],[0.653,0.488,1]])
w1=0,1
w2=1,2
w3=3,1
x4=map( lambda x:x[0]+x[1],data_set)
net=map( lambda x:x[0]*w1+x[1]*w2+x[2]*w3,data_set)
''' print(x3)
print(w)'''
#print(net) 
plt(data_set)
for i in data_set:
    for j in i:
        for z in i:
            print(z)
    print('------')    


y=[];
for i in x4:
    if(i>1):
        y.append(1)
    else:
        y.append(-1)    
#print(y)
            



 


