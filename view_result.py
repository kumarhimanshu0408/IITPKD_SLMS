from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class ViewResultClass:
    def __init__(self,root,dash=None):
        self.dash=dash
        self.root=root
        self.root.title("View Student Result")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        self.course_list=[]
        self.var_course=StringVar()

        file=open("user.txt","r")
        self.Email=file.read()
        file.close()
        content=sqlite3.connect(database="SLMS.DataBase")
        cur=content.cursor()
        cur.execute("select name from student1 where email=?",(self.Email,))
        row=cur.fetchone()
        self.name=row[0]


        #......title...........
        title=Label(self.root,text="View Student Result",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)

        #.................searchpanels........................
        self.var_id=""
        self.var_searchroll=StringVar()
        lbl_search_roll=Label(self.root,text="Search By Roll No.",font=("goudy old style",20,"bold"),bg="white").place(x=280,y=100)
        lbl_select_course=Label(self.root,text="Select Course.",font=("goudy old style",20,"bold"),bg="white").place(x=335,y=150)
        self.course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",20,'bold'),state='readonly',justify=CENTER)
        self.course.place(x=520,y=150,width=150)
        self.show_btn=Button(self.root,text="Show result",font=("goudy old style",15,"bold"),bg="#03a9f4",cursor="hand2",command=self.show_result).place(x=690,y=150)

        txt_search_roll=Entry(self.root,textvariable=self.var_searchroll,font=("goudy old style",20),bg="lightyellow").place(x=520,y=100,width=150)
        #...........search&clearbutton..........
        btn_search=Button(self.root,text='search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=680,y=100,width=100,height=35)
        btn_clear=Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2",command=self.clear).place(x=800,y=100,width=100,height=35)

        #...........labels..............
        lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50) 
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_marksobtained=Label(self.root,text="Marks Obtained",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        lbl_totalmarks=Label(self.root,text="Total Marks",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        lbl_percent=Label(self.root,text="Percentage",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)


        self.txt_roll=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.txt_roll.place(x=150,y=280,width=150,height=50) 
        self.txt_name=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.txt_name.place(x=300,y=280,width=150,height=50)
        self.txt_course=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.txt_course.place(x=450,y=280,width=150,height=50)
        self.txt_marksobtained=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.txt_marksobtained.place(x=600,y=280,width=150,height=50)
        self.txt_totalmarks=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.txt_totalmarks.place(x=750,y=280,width=150,height=50)
        self.txt_percent=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.txt_percent.place(x=900,y=280,width=150,height=50)              
        

        #................deletebutton..............
        btn_delete=Button(self.root,text='Delete',font=("goudy old style",15,"bold"),bg="red",activebackground="lightgray",fg="white",cursor="hand2",command=self.delete).place(x=500,y=350,width=150,height=35)
        

    #...........................................................
    def search(self):
        content=sqlite3.connect(database="SLMS.DataBase")
        cur=content.cursor()
        try:
            if self.var_searchroll.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            else:
                cur.execute("select course,name from result where roll=?",(self.var_searchroll.get(),))
                row=cur.fetchall()
                print(row)
                if row!=None:
                    self.course_list=[]
                    for r in row:
                        print(r[0])
                        self.course_list.append(r[0])
                    self.course['values']=self.course_list
                    self.txt_name.config(text=row[0][1])
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def clear(self):
            self.var_id=""
            self.txt_roll.config(text="")
            self.txt_name.config(text="")
            self.txt_course.config(text="")
            self.txt_marksobtained.config(text="")
            self.txt_totalmarks.config(text="")
            self.txt_percent.config(text="")
            self.course.config(values=[])


    def show_result(self):
        content=sqlite3.connect(database="SLMS.DataBase")
        cur=content.cursor()
        try:
            if self.var_searchroll.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_searchroll.get(),self.var_course.get()))
                row=cur.fetchone()
                print(row)
                if row!=None:
                    self.var_id=row[0]
                    self.txt_roll.config(text=row[1])
                    self.txt_name.config(text=row[2])
                    self.txt_course.config(text=row[3])
                    self.txt_marksobtained.config(text=row[4])
                    self.txt_totalmarks.config(text=row[5])
                    self.txt_percent.config(text=row[6])
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def delete(self):
        content=sqlite3.connect(database="SLMS.DataBase")
        cur=content.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search Student Result First",parent=self.root)
            elif(self.name !=self.txt_name.cget('text')):
                messagebox.showerror("Error","Can't change other's result",parent=self.root)
            else:
                cur.execute("select * from result where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        content.commit()
                        messagebox.showinfo("Delete","Result deleted  Successfully",parent=self.root)
                        if self.dash !=None:
                            self.dash.check_update()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


        





if __name__=="__main__":
    root=Tk()
    obj=ViewResultClass(root)
    root.mainloop()