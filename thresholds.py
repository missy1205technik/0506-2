import cv2
import tkinter as tk
from tkinter import messagebox
import time
import sys


class Input:
    val = 80
    
    def __init__(self):
        
        self.root = tk.Tk()                
        self.root.title('しきい値')       
        self.root.geometry('300x300')
        
        
    def sel(self):
        self.selection = "Value = " + str(self.var.get())
        self.val=self.var.get()

        self.label.config(text=self.selection)
        print(self.selection)
        print(type(self. val))
        print(self.val)
        return(self.val)
        # file= open('ts.data','a+')
        # file.write(str(self.val))
        # file.close()
        


    def end_button(self):
        answer = messagebox.askyesno('確認','終了しますか？')
        if answer == True:
            file= open('ts.data','w')
            file.write(str(self.val))
            file.close()
            
            self.root.withdraw()
            self.root.quit()
        
    def main(self):        
        #global root
        self.var = tk.DoubleVar()
        self.scale = tk.Scale(self.root, variable=self.var)
        self.scale.pack(padx=5, pady=5, anchor=tk.CENTER)

        button = tk.Button(self.root, text="閾値設定", command=self.sel)
        button.pack(padx=5, pady=5,fill=tk.X)

        self.label = tk.Label(self.root)        
        self.label.pack(padx=5, pady=5,fill=tk.X)
        
        quit_button = tk.Button(self.root, text="終了", command=self.end_button)
        quit_button.pack(padx=5, pady=5,fill=tk.X)

        self.root.mainloop()

if __name__ == '__main__':   
    inp = Input()
    inp.main()
    

    
    
