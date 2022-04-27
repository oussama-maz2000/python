import numpy as np

x1=np.array([[0.325,0.768,1],[0.798,0.821,1]
             ,[0.364,0.417,1],[0.241,0.605,1]
             ,[0.653,0.488,1]])
x2=[[0.325,0.768,1],[0.798,0.821,1]
             ,[0.364,0.417,1],[0.241,0.605,1]
             ,[0.653,0.488,1]]
print(type(x2))
    
def sum_Y(list):
    sum=map( lambda x:x[0]+x[1],x1)
    y=[];
    for i in sum:
        if(i>1):
            y.append(1)
        else:
            y.append(-1)
    print(y)        
sum_Y(x1)