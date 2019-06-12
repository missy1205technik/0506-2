
import cv2
import copy
import numpy as np
import sys
import time


file = open('ts.data','r')
ts = file.read()

print('VAL='+str(ts))


#画像をグレースケールで読み込む
img = cv2.imread("img.png", 0)
temp = cv2.imread("temp.png", 0)
#マッチングテンプレートを実行
#比較方法はcv2.TM_CCOEFF_NORMEDを選択
result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
#検出結果から検出領域の位置を取得
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
w, h = temp.shape[::-1]
bottom_right = (top_left[0] + w, top_left[1] + h)
#検出領域を四角で囲んで保存
result = cv2.imread("img.png")
cv2.rectangle(result,top_left, bottom_right, (255, 0, 0), 2)
cv2.imwrite("result.png", result)





class Match():
    def main(self):
        temp_gray = cv2.imread('temp.png',0)
        temp = cv2.imread('temp.png')
        cap = cv2.VideoCapture(0)
        
        
        while True:
            ret, frame = cap.read()
            cv2.namedWindow('frame',cv2.WINDOW_GUI_NORMAL)
            cv2.moveWindow('frame',0,-10)
            #frame =cv2.resize(frame, dsize=None, fx=0.6, fy=0.6)
            cv2.imshow('frame',frame)

            key=cv2.waitKey(1) & 0xFF
            if key == ord('t'): 
                ret, frame = cap.read()           
                fframe = frame.copy()
                img = fframe
                gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  
                
                def matching(gray, temp_gray,):
                    
                    #マッチングテンプレートを実行
                    result = cv2.matchTemplate(gray, temp_gray, cv2.TM_CCOEFF_NORMED)
                    min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(result)

                    w, h = temp_gray.shape[::-1]
                    pt=max_pt
                    print(pt,w,h,max_value)

                    threshold = float(ts)
                    print("test:"+ts)
                    loc = np.where(result >= threshold)
                    

                    def show_result(img):

                        cv2.namedWindow('out',cv2.WINDOW_NORMAL)
                        cv2.moveWindow('out',0,-10)
                        #img =cv2.resize(img, dsize=None, fx=1, fy=1)
                        cv2.imshow('out',img)

                    if max_value >= threshold:
                        cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h),(0,255,0),2)
                        cv2.putText(img, str("{:.2f}".format(max_value*100)+"% OK"), (100, 80), cv2.FONT_HERSHEY_COMPLEX,3, (0, 255,0),2,cv2.LINE_AA)    

                    else:
                        cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h),(0,0,255),2)
                        cv2.putText(img, str("{:.2f}".format(max_value*100)+"% NG"), (100, 100), cv2.FONT_HERSHEY_COMPLEX,3, (0, 0, 255),2,cv2.LINE_AA)    
                        
                    show_result(img)

                matching(gray, temp_gray)
                

            if key == ord('q'):

                cv2.destroyAllWindows()
                cap.release()
                cv2.waitKey() & 0xFF
    
if __name__ == '__main__':   
    mc = Match()
    mc.main()


