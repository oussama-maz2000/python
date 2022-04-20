import numpy as np
x3=np.random.random_integers(7,size=(4,2))
w=np.random.random((4,2))
x4=map( lambda x:x[0]+x[1],x3)
net=map( lambda x,w:[x[0]*w[0],x[1]*w[1]],x3,w)
print(x3)
print(w)
print(net)


y=[];
for i in x4:
    if(i>5):
        y.append(1)
    else:
        y.append(-1)    

            



 


