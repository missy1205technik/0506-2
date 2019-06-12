
import copy
import cv2
import numpy as np
import time
import tkinter as tk
from tkinter import messagebox

class Template:

    def __init__(self):
        root = tk.Tk()
        root.withdraw()  
        
    def capture_start(self):
        self.cap = cv2.VideoCapture(0)
        
    def capture_release(self):
        self.cap.release()
        
    def capture(self):
        # フレームをキャプチャする        
        ret, frame = self.cap.read()
        return ret, frame
        
def display(label,frame):
    
    cv2.moveWindow(label,0,-10)
    cv2.imshow(label,frame)

def click_and_crop(event, x, y, flags, param):
    
    global refPt, cropping, image

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append ((x, y))
        cropping = False

        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        display('image',image)

    
def main():
    global image, refPt
    tp = Template()
    tp.capture_start()
    
    
    while True:
        
        # フレームをキャプチャする
        ret, frame = tp.capture()
        display('frame',frame)
        
        # キーボード入力待ち
        key=cv2.waitKey(1) & 0xFF

        # qが押された場合は終了する
        if key == 27:
            break

        if key == ord('t'):
            #fframe = frame.copy()
            refPt = []

            # load the image, clone it, and setup the mouse callback function
            image = frame
            clone = image.copy()
            cv2.namedWindow('image',cv2.WINDOW_NORMAL)
            cv2.setMouseCallback('image', click_and_crop)


            while True:
                display('image',image)

                
                key = cv2.waitKey(0) & 0xFF
                print('OK')
                # if the 'r' key is pressed, reset the cropping region
                if key == ord('r'):
                    image = clone.copy()

                elif key == ord('c'):
                    break

            if len(refPt) == 2:
                roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
                cv2.imshow("ROI", roi)
                cv2.imwrite('temp.png',roi)
                messagebox.showinfo('終了', '画像の登録が完了しました！')
                break

    cv2.waitKey(1)        
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    tp.capture_release()
        



if __name__ == '__main__':   
    main()
    
