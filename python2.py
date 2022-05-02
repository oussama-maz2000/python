""" from tkinter import Frame , Canvas,CENTER,ROUND
from PIL import Image , ImageTk 
import cv2

class ImageViewer(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master=master,bg='gray',width=600,height=600)

        self.canvas = Canvas(self, bg="gray", width=600, height=400)
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.shown_image = None
        self.x = 0
        self.y = 0
        self.crop_start_x = 0
        self.crop_start_y = 0
        self.crop_end_x = 0
        self.crop_end_y = 0
        self.draw_ids = list()
        self.rectangle_id = 0
        self.ratio = 0 """
from mimetypes import init
from traceback import print_tb
from matplotlib.pyplot import get
import numpy as np

Data_set=np.array([[0.325,0.768],
                   [0.798,0.821]
                  ,[0.364,0.417],
                   [0.241,0.605]
                  ,[0.653,0.488]])

''' class x1:
    def __init__(self,data):
        self.data=data;
    def sum(self):
        print(self.data)
test=x1(Data_set);
test.sum(); '''

w=np.array([[1.2,0.1],[1.2,0.1],[1.2,0.1],[1.2,0.1],[1.2,0.1]])

sum=(Data_set*w)+1.2;
x4=map( lambda x:x[0]+x[1],sum)
rnf=np.random.random(size=(Data_set.shape))
weights = [0 for i in range(len(Data_set[0]))]


def init_wights_and_bias(data_length):
    wights=np.random.random(size=(data_length))
    wight_bias=0.5;
    return wights,wight_bias;
wigth=init_wights_and_bias(5)
print(wigth)
#print(x4)
