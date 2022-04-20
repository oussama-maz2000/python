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

data =[
    [255,0,255],
    [255,0,255],
    [255,0,255],
    [255,0,255],
],
[
    [255,0,255],
    [255,0,255],
    [255,0,255],
    [255,0,255],
],
