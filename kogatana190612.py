
import cv2
import numpy as np
from PIL import Image, ImageTk
import subprocess
import sys
import time
import tkinter as tk
from tkinter import messagebox

import TempCrop as temp_c
from match0330OK import Match
from thresholds import Input 


root = tk.Tk()
root.title('KoGATANA')
root.geometry('160x480+640+0')


def temp_crop():   
    temp_c.main()
       
def matching():
    global temppic, canvas
    temppic = tk.PhotoImage(file="temp.png")
    canvas.itemconfig("pic", image=temppic, anchor=tk.NW)
    mc = Match()
    mc.main()

def sub_quit():
    answer = messagebox.askyesno('確認','終了しますか？')
    if answer == True:
        time.sleep(3)
        quit()
        #subprocess.run(('sudo','shutdown','-h','now'))       

def value():
     

    inp = Input()
    inp.main()
    print(inp.val)
    
# Buttonを設置してみる
temp_crop_button = tk.Button(text='範囲選択',font=("",16),bg="LightBlue1",activeforeground = 'green',command=temp_crop)
temp_crop_button.pack(fill='both')

matching_button = tk.Button(text='マッチング',font=("",16),bg="LightBlue1",activeforeground = 'green',command=matching)
matching_button.pack(fill='both')

value_button = tk.Button(text='しきい値設定',font=("",16),bg="LightBlue1",activeforeground = 'green',command=value)
value_button.pack(fill='both')

sub_quit_button = tk.Button(text='終了',font=("",16),bg="LightBlue1",activeforeground = 'green',command=sub_quit)
sub_quit_button.pack(fill='both')
#キャンバスエリア
temppic = tk.PhotoImage(file="temp.png")

canvas = tk.Canvas(width=155, height=200)

canvas.place(x=10, y=250)
canvas.pack()
canvas.create_image(0,0, image=temppic, anchor=tk.NW, tags='pic')

root.mainloop()

#if __name__ == '__main__':   
   

