from unittest import result
import numpy as np

data=[[-1,-1,1,-1],[-1,1,1,1]]

def init_weights_and_weight_bias(data_length):
    #initiliz the weights and bias weight
    weights=np.random.random(size=(data_length))
    weights_bias=0.5;
    # return array of the all  weights
    return [weights,weights_bias];


# function caluculate the sum of weight*input and return 1 or -1 it depends on condition
def sign(rows,weights,w_bias):
    first_value=rows[0]*weights[0]
    second_value=rows[1]*weights[1]
    sum=w_bias+second_value+first_value;
    return 1 if sum>0 else -1;   

def perceptron(data):
    
    alpha=0.01 # it's learning step
    final_resulat=''
    [weights,weights_bias]=init_weights_and_weight_bias(len(data[0]))
    error=0
    while True:
        iscorrect=True; # to make tests
        for i in range (0,len(data)):
            expected=data[i][3] # exprected variable it's the class row in your quiz
            predicted=sign(data[i],weights,weights_bias) #  predicted it's Y 
            if expected != predicted :
                error +=1;
                iscorrect=False;
                
                # block of update the weight in cas if we find error 
                weights[0]=weights[0]+(alpha*(expected-predicted)*data[i][0])
                weights[1]=weights[1]+(alpha*(expected-predicted)*data[i][1])
                weights_bias=weights_bias+(alpha*(expected-predicted)*data[i][2])
                print(error)
            if iscorrect:
                # if we get everything correct after the (if expected != predicted :) condition 
                final_resulat += str(weights[0]) + ' , ' + str(weights[1]) + ' , ' +str(weights[2])  
                break;
            return final_resulat;
        
result=perceptron(data);
print(result)