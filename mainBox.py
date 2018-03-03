#Face Detection and Recognization for Autonomous Attendance 
from tkinter import *
import cv2
import numpy as np

class progress:
    def detect():
        FaceDetect = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
        cam = cv2.VideoCapture(0)
        id=input("Enter your roll number :")
        sampleNum=0
        while True:
            ret,img = cam.read()
            gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
            faces = FaceDetect.detectMultiScale(gray,1.3,5)
            for (x,y,w,h) in faces:
                sampleNum+=1
                cv2.imwrite("MyDataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.waitKey(1)
            cv2.imshow("Face",img)
            cv2.waitKey(1)
            if sampleNum>20:
                break
        cam.release()
        cv2.destroyAllWindows()
    def step1(master):
        #***** ENTRIES *****
        #mainFrame = Frame(master,width=1000,height=1000)
        #logValue=0
        lbl_username = Label(master,text="Username").place(x=60,y=20)
        lbl_password = Label(master,text="Password").place(x=60,y=45)
        entry_usr= Entry(master)
        entry_usr.place(x=135,y=20)
        entry_pass= Entry(master,show="*")
        entry_pass.place(x=135,y=45)
        
        #*****DROP DOWNS*****
        branch_value = StringVar(master)
        branch_value.set("IT")
        class_value =StringVar(master)
        class_value.set("SY")
        
        optionbr= OptionMenu(master,branch_value,"Mechanical","Civil","Electrical","IT","ENTC")
        optionbr.place(x=160,y=85)
        optioncl= OptionMenu(master,class_value,"FY","SY","TY","BE")
        optioncl.place(x=160,y=120)
        
        def check(master):
            #right now value of entry_user is not shubham 
            if (entry_usr.get() == "shubham") and (entry_pass.get()=="pass"):
                    """loginmsg= "You are logged in!"
                    msg= Message(master,text=loginmsg,anchor=W)
                    msg.config(fg='red', font=('times', 13, 'italic'))
                    msg.place(x=150,y=160)"""
                    #self.detect()
                    #nonlocal logValue=1
            else:
                loginmsg= "Wrong credentials try again!"
                msg= Message(master,text=loginmsg,anchor=W)
                msg.config(fg='red', font=('times', 10, 'italic'))
                msg.place(x=150,y=160)
        loginButton = Button(master,text="Login",command=lambda :check(master),bg="SteelBlue1").place(x=160,y=220)



        
    
root= Tk()
root.geometry('400x300+500+200')
root.title('FDRA2')

p=progress
p.step1(root)
"""if nonlocal logValue==1:
    p.detect()"""
p.detect()

root.mainloop()