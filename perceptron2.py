import numpy as np

Data_set=np.array([[0.325,0.768,1],[0.798,0.821,1]
             ,[0.364,0.417,1],[0.241,0.605,1]
             ,[0.653,0.488,1]])
      

class Neuron :
    alpha=0.01;
    output=[];
    def __init__(self,data) :
        self.data=data;
        self.bias=0.5;
        self.wights=np.random.random();
    
    def sum_output(self):
         out=(self.data*self.wights)+self.bias;
         for i in out:
             if(i>0):
                 self.output.append(1)
             else:
                 self.output.append(-1)
             
         
        
        
        
    
