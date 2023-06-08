from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class ResultClass:
    def __init__(self,root,dash=None):
        self.dash=dash
        self.root=root
        self.root.title("Result")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        file=open("user.txt","r")
        self.Email=file.read()
        file.close()
        self.name=""
        self.rollno=0
        self.fetchname()


        #......title...........
        title=Label(self.root,text="Add Student's Result",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)

        #..................labels.................
        lbl_select=Label(self.root,text="Select Course",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=100)
        lbl_name=Label(self.root,text=self.name,font=("goudy old style",20,"bold"),bg="white").place(x=200,y=160)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=220)
        lbl_marksobtained=Label(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=280)
        lbl_fullmarks=Label(self.root,text="Full Marks",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=340)


        #..............Variables...............
        self.var_course=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marksobtained=StringVar()
        self.var_fullmarks=StringVar()
        self.course_list=[]
        self.fetch_roll()

        
        #...........EntryFields................
        self.txt_select=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
        self.txt_select.place(x=280,y=100,width=320)
        self.txt_select.set("Select")   #............searchbutton.................
        txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20,'bold'),bg='lightyellow',state="readonly").place(x=280,y=220,width=320)
        txt_marksobtained=Entry(self.root,textvariable=self.var_marksobtained,font=("goudy old style",20,'bold'),bg='lightyellow').place(x=280,y=280,width=320)
        txt_fullmarks=Entry(self.root,textvariable=self.var_fullmarks,font=("goudy old style",20,'bold'),bg='lightyellow').place(x=280,y=340,width=320)


        #...........button...........
        btn_submit=Button(self.root,text="Submit",font=("times now roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",font=("times now roman",15),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)
        
        #............adding_photo...............
        self.bg_image=Image.open(r"C:\Users\himan\OneDrive\Desktop\1st app\result.jpg")
        self.bg_image=self.bg_image.resize((500,300),Image.ANTIALIAS)
        self.bg_image=ImageTk.PhotoImage(self.bg_image)
        self.lbl_bg=Label(self.root,image=self.bg_image).place(x=650,y=100)

#...............dtataken started....................
    def fetchname(self):
        content=sqlite3.connect(database="SLMS.DataBase")
        cur=content.cursor()
        cur.execute("select * from student1 where email=?",(self.Email,))
        row=cur.fetchone()
        self.name=row[1]
        self.rollno=row[0]
        print(self.rollno)


    def fetch_roll(self):
        content=sqlite3.connect(database="SLMS.DataBase")
        cur=content.cursor()
        try:
            cur.execute("select name from course where studentemail=?",(self.Email,))
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def add(self):
        content=sqlite3.connect(database="SLMS.DataBase")
        cur=content.cursor()
        try:
            if self.var_name.get()=="select":
                messagebox.showerror("Error","Please first search student record",parent=self.root)
            else:
                cur.execute("select * from result where name=? and course=?",(self.name,self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already present",parent=self.root)
                else:
                    percent=round((int(self.var_marksobtained.get())*100)/(int(self.var_fullmarks.get())),2)
                    cur.execute("insert into result (roll,name,course,marksobtained,fullmarks,percent) values(?,?,?,?,?,?)",(self.rollno,self.name,self.var_course.get(),self.var_marksobtained.get(),self.var_fullmarks.get(),str(percent)))
                    content.commit()
                    messagebox.showinfo("Success","Result Added Successfully",parent=self.root)
                    if self.dash !=None:
                            self.dash.check_update()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def clear(self):
        self.var_course.set("select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marksobtained.set("")
        self.var_fullmarks.set("")


if __name__=="__main__":
    root=Tk()
    obj=ResultClass(root)
    root.mainloop()