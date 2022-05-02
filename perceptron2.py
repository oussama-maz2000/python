from random import random
from matplotlib.pyplot import step
import numpy as np

Data_set=[[0.325,0.768,1],[0.798,0.821,1],[0.364,0.417,1],[0.241,0.605,1],[0.653,0.488,1]]

def init_wights_and_bias(data_length):
    wights=np.random.random(size=(data_length))
    wight_bias=0.5;
    return wights,wight_bias;

def sign(rows,wights,w_bias):
    first_value=rows[0]*wights[0]
    second_value=rows[1]*wights[1]
    sum=w_bias+second_value+first_value;
    return 1 if sum>0 else -1;   

        