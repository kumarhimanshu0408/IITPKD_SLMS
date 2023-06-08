import sqlite3
from tkinter import*
from PIL import Image,ImageTk
from course import CourseClass
from student import StudentClass
from result import ResultClass
from view_result import ViewResultClass
import subprocess,sys
from threading import Thread
import VoioceAssistant as Va

def close():
    sys.exit(0)



class StudentLearningManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("SLMS")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.voiceOn=False


        #..........icons........
        self.logo_dash=ImageTk.PhotoImage(file="imresizer-1685361651808.jpg")

        #................left =image...........................
        self.left=ImageTk.PhotoImage(file="imresizer-1685809861300.jpg")
        left=Label(self.root,image=self.left,bd=6).place(x=15,y=180,width=380,height=450)


        #......title...........
        title=Label(self.root,text="Student Learning Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)


        #.....menu.....
        m_frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        m_frame.place(x=10,y=70,widt=1340,height=80)

        btn_course=Button(m_frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(m_frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(m_frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(m_frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.view_result).place(x=680,y=5,width=200,height=40)
        btn_logout=Button(m_frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_exit=Button(m_frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit).place(x=1120,y=5,width=200,height=40)


        #.....content_window.....
        self.bg_image=Image.open("1604730708.jpg")
        self.bg_image=self.bg_image.resize((920,350),Image.ANTIALIAS)
        self.bg_image=ImageTk.PhotoImage(self.bg_image)

        self.lbl_bg=Label(self.root,image=self.bg_image).place(x=400,y=180,width=920,height=350)

        #.....update_details....
        
        self.lbl_course=Label(self.root,font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_student=Label(self.root,font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=100)

        self.lbl_result=Label(self.root,font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)
        self.check_update()


        # gyaani____
        alexa=Image.open("alexa.jpeg")
        alexa=alexa.resize((40,40))
        img_alex=ImageTk.PhotoImage(alexa)
        self.gyaani_btn=Button(self.root,image=img_alex,bg="white",cursor="hand2",command=self.gyaani).place(x=1300,y=2)

        lbl_gyaani=Label(self.root,text="Ask 'GYAANI'",font=("goudy old style",14),bg="white",bd=0).place(x=1230,y=50)

        self.recog_label=Label(self.root,text="",bg="red")
        self.recog_label.place(x=1270,y=20,width=12,height=12)

        #....footer.....
        title=Label(self.root,text="IIT PKD-SLMS(Learning Management System:Students Affairs)\nContact Us for any Technical Issue:9110948964",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.root.mainloop()

    def check_update(self):
        content=sqlite3.connect(database="SLMS.Database")
        cur=content.cursor()
        cur.execute("select * from course")
        row=cur.fetchall()
        self.total_course=len(row)
        self.lbl_course.config(text=f"Total Courses\n[{self.total_course}]")
        cur.execute("select * from student1")
        row=cur.fetchall()
        self.total_student=len(row)
        self.lbl_student.config(text=f"Total Student\n[{self.total_student}]")
        cur.execute("select * from result")
        row=cur.fetchall()
        self.total_result=len(row)
        self.lbl_result.config(text=f"Total Results\n[{self.total_result}]")

    def call_assistence(self):
        print("calling voice assistance")
        Va.text_to_speech("HI this is GYAANI\n How may I assist you")
        toDo=Va.voiceAssist(self.recog_label)
        print(toDo,"mm")
        if toDo==False:
            self.voiceOn=False
        elif toDo=="exit":
            self.exit()
            self.voiceOn=False
        elif toDo=="course":
            self.add_course()
            self.voiceOn=False
        elif toDo=="student":
            self.add_student()
            self.voiceOn=False
        elif toDo=="result":
            self.add_result()
            self.voiceOn=False
        elif toDo=="vresult":
            self.view_result()
            self.voiceOn=False

    def gyaani(self):
        print("HEllo from assistance")
        if not Va.isgood:
            self.voiceOn=False
        if not self.voiceOn:
            self.recog_label.config(bg="green")
            self.thread=Thread(target=self.call_assistence)
            self.thread.start()
        else:
            Va.close()
            self.recog_label.config(bg="red")

            
        self.voiceOn=not self.voiceOn

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win,self)
        self.check_update()
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win,self)
        self.check_update()
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win,self)
        self.check_update()
    def view_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ViewResultClass(self.new_win,self)
        self.check_update()

    def logout(self):
        file=open("user.txt","w")
        print("",end="",file=file)
        file.close()
        root.destroy()
        subprocess.call(["python","login.py"])

    def exit(self):
        file=open("user.txt","w")
        print("",end="",file=file)
        file.close()
        print("closing")
        Va.close()
        sys.exit(0)


if __name__=="__main__":
    root=Tk()
    obj=StudentLearningManagementSystem(root)
    