import numpy as np

x1=np.random.random((3,1));
x2=np.random.random((3,1));
x3=x1+x2;
x4=[]
print(x3);
for i in x3:
    if(i>1):
        x4.append(1);
    else:
        x4.append(-1);
    
print(x4);
