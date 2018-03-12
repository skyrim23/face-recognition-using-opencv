import cv2
import numpy as np
import urllib.request as ur
from xlutils.copy import copy
import xlrd
from datetime import date
import sqlite3
import matplotlib.pyplot as plt

global present
#initialize list of 23 elements
present = [0]*23

def detector():
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    rec=cv2.face.LBPHFaceRecognizer_create();
    rec.read("recognizer/trainingData.yml")
    ID=0
    font=cv2.FONT_HERSHEY_SIMPLEX
    url='http://192.168.43.1:8080/shot.jpg'
    imgr=ur.urlopen(url)
    while True:
        imgr=ur.urlopen(url)
        imgnp=np.array(bytearray(imgr.read()),dtype=np.uint8)
        img=cv2.imdecode(imgnp,-1)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            ID,conf=rec.predict(gray[y:y+h,x:x+w])
            cv2.putText(img,str(ID),(x,y+h),font,5,(0,255,0));
            present[ID] =1 
            
        cv2.imshow("Face",img);
        if(cv2.waitKey(1)==ord('q')):
            break;
    cv2.destroyAllWindows()


def excel():
    conn=sqlite3.connect("FaceBase.db")

    r=0
    #retrieve value of c from db
    cmd="SELECT c FROM Counter"
    cursor = conn.execute(cmd)
    c=cursor.fetchone()
    cnt=c[0]
    print(str(cnt))
     #reset value in counter to '2'
    #cmd="UPDATE Counter SET c ="+str(2)    
    cmd="UPDATE Counter SET c ="+str(cnt+1)
    conn.execute(cmd)
    conn.commit()
    conn.close()
    date1= date.today()
    rb= xlrd.open_workbook('student.xls')
    wb= copy(rb)
    
    w_sheet=wb.get_sheet(0)
    w_sheet.write(r,cnt,str(date1))
    r+=1
    pre = present
    #print(str(date1))
    for i in pre:
        if i==1:
           w_sheet.write(r,cnt ,'P')
           r+=1
        else :
            w_sheet.write(r,cnt ,'A')
            r+=1
    
    #c[0]+=1       
    
    wb.save('student.xls')     
 
def display_plot(n):
        rb= xlrd.open_workbook('student.xls')
        worksheet = rb.sheet_by_index(0)
        rows= worksheet.nrows
        cols=worksheet.ncols
        global result_data
        result_data=[]
        global row_data
        row_data=[]
        for cur_r in range(1,rows,1):
            row_data=[]
            
            for cur_c in range(2,cols,1):
                data = worksheet.cell_value(cur_r,cur_c)
                row_data.append(data)
            result_data.append(row_data)
        pre_cnt=[]
        for d in result_data:
            cnt=0
            for a in d: 
                #print(str(a))
                if a=='P':
                    cnt+=1
            pre_cnt.append(cnt)
        #print(str(pre_cnt))
        hist_data = []
        count=0
        for i in pre_cnt :
            hist_data.append(int((i/(cols-2))*100))
            count+=1
            
        print(str(hist_data))
        a = np.asarray(hist_data)
        xtick=[]
        for i in range(1,rows):
            xtick.append(i)
        ytick=[]
        for i in range(10,110,10):
            ytick.append(i)
        if n == -1:

            #plt.bar(5,[420,20],animated=1)

            #plt.xticks(xtick, xtick)
            #plt.yticks(ytick,ytick)
            #plt.bar(rows-1,a,animated=1)

            plt.hist(a,bins=rows-1)
            plt.show()

        
    
    
#detector()
excel()

ch=int(input("you want to display :\n1.All rows 2.one row  3.more than one row"))
if ch==1:

    display_plot(-1)
elif ch==2:
    n = int(input("Enter row you want to display:"))
    display_plot(n)
else :
    n =int(input("Enter all rows you want to display:"))
    display_plot(n)
