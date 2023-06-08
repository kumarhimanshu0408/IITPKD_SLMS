import subprocess
import sys
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class StudentClass:
    def __init__(self,root,dash=None):
        self.dash=dash
        self.root=root
        self.root.title("Student")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        file=open("user.txt","r")
        self.Email=file.read()
        file.close()


        #......title...........
        title=Label(self.root,text="Manage Student Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)

        #........variables.....
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
    

        #........widget........
        #........column1.............
        lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=60)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=100)
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=140)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=180)
        lbl_state=Label(self.root,text="State",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=220)
        lbl_adress=Label(self.root,text="Address",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=260)

        
        

        #.........entry_fields_column1.......
        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_roll.place(x=150,y=60,width=200)
        self.txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_name.place(x=150,y=100,width=200)
        self.txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_email.place(x=150,y=140,width=200)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","MALE","FEMALE","TRANS"),font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
        self.txt_gender.place(x=150,y=180,width=200)
        self.txt_gender.current(0)
        self.txt_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_state.place(x=150,y=220,width=150)



        #........column2.............
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15,'bold'),bg='white').place(x=360,y=60)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,'bold'),bg='white').place(x=360,y=100)
        lbl_admission=Label(self.root,text="Admission",font=("goudy old style",15,'bold'),bg='white').place(x=360,y=140)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,'bold'),bg='white').place(x=360,y=180)
        lbl_city=Label(self.root,text="City",font=("goudy old style",15,'bold'),bg='white').place(x=310,y=220)
        lbl_pin=Label(self.root,text="Pin",font=("goudy old style",15,'bold'),bg='white').place(x=500,y=220)
        

        #.........entry_fields_column2.......
        self.course_list=[]
        #function_call to update the list
        self.fetch_course()
        self.txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_dob.place(x=480,y=60,width=200)
        self.txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_contact.place(x=480,y=100,width=200)
        self.txt_admission=Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_admission.place(x=480,y=140,width=200)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
        self.txt_course.place(x=480,y=180,width=200)
        self.txt_course.set("Select")
        self.txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_city.place(x=380,y=220,width=100)
        self.txt_pin=Entry(self.root,textvariable=self.var_pin,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_pin.place(x=560,y=220,width=120)
        #...................Text Adresss....................
        
        self.txt_adress=Text(self.root,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_adress.place(x=150,y=265,width=540,height=100)
        

        #......buttons........
        self.btn_update=Button(self.root,text='Update',font=("goudy old style",15,"bold"),bg="green",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=150,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text='Delete',font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=270,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=390,y=400,width=110,height=40)


        #........search_panels......
        self.var_search=StringVar()
        lbl_search_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,'bold'),bg='white').place(x=720,y=60)
        txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg='lightyellow')
        txt_search_roll.place(x=870,y=60,width=180)
        btn_search=Button(self.root,text='search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        btn_search.place(x=1070,y=60,width=110,height=28)

        #........content.......
        self.c_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=720,y=100,width=470,height=340)
        
        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.c_frame,orient=HORIZONTAL)
        self.course_table=ttk.Treeview(self.c_frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","adress"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrollx.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.course_table.xview)
        scrolly.config(command=self.course_table.yview)

        self.course_table.heading("roll",text="Roll No.")
        self.course_table.heading("name",text="Name")
        self.course_table.heading("email",text="Email")
        self.course_table.heading("gender",text="Gender")
        self.course_table.heading("dob",text="D.O.B")
        self.course_table.heading("contact",text="Contact")
        self.course_table.heading("admission",text="Admission")
        self.course_table.heading("course",text="Course")
        self.course_table.heading("state",text="State")
        self.course_table.heading("city",text="City")
        self.course_table.heading("pin",text="PIN")
        self.course_table.heading("adress",text="Address")
        
        self.course_table['show']='headings'
        self.course_table.column("roll",width=100)
        self.course_table.column("name",width=100)
        self.course_table.column("email",width=100)
        self.course_table.column("gender",width=100)
        self.course_table.column("dob",width=100)
        self.course_table.column("contact",width=100)
        self.course_table.column("admission",width=100)
        self.course_table.column("course",width=100)
        self.course_table.column("state",width=100)
        self.course_table.column("city",width=100)
        self.course_table.column("pin",width=100)
        self.course_table.column("adress",width=200)
        self.course_table.pack(fill=BOTH,expand=1)
        self.course_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#..................................................................
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_adress.delete('1.0',END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")
        

    def delete(self):
        content=sqlite3.connect(database="SLMS.DataBase")
        content1=sqlite3.connect(database="login.database")
        cur1=content1.cursor()
        cur=content.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            else:
                cur.execute("select * from student1 where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","please select student from the list first",parent=self.root)
                elif row[2] != self.Email:
                    messagebox.showerror("Error","You cannot delete other's account.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?\n NOTE: This will delete all the courses and result associated with this account(student)!",parent=self.root)
                    if op==True:
                        cur.execute("delete from student1 where roll=?",(self.var_roll.get(),))
                        cur.execute("delete from course where studentemail=?",(self.Email,))
                        cur.execute("delete from result where roll=?",(self.var_roll.get(),))
                        cur1.execute("delete from student where email=?",(self.Email,))
                        content.commit()
                        content1.commit()
                        messagebox.showinfo("Delete","Student Data deleted  Successfully",parent=self.root)
                        self.root.destroy()
                        print("dash")
                        self.dash.exit()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def readonly(self):
        self.txt_adress.config(state='disabled')
        self.txt_city.config(state='disabled')
        self.txt_state.config(state='disabled')
        self.txt_email.config(state='disabled')
        self.txt_course.config(state='disabled')
        self.txt_gender.config(state='disabled')
        self.txt_name.config(state='disabled')
        self.txt_dob.config(state='disabled')
        self.txt_admission.config(state='disabled')
        self.txt_pin.config(state='disabled')
        self.txt_contact.config(state='disabled')

    def noreadonly(self):
        self.txt_adress.config(state='normal')
        self.txt_city.config(state='normal')
        self.txt_state.config(state='normal')
        self.txt_email.config(state='normal')
        self.txt_name.config(state='normal')
        self.txt_dob.config(state='normal')
        self.txt_admission.config(state='normal')
        self.txt_pin.config(state='normal')
        self.txt_contact.config(state='normal')
        self.txt_course.config(state='readonly')
        self.txt_gender.config(state='readonly')

    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        self.txt_roll
        r=self.course_table.focus()
        cont=self.course_table.item(r)
        row=cont["values"]
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.txt_adress.delete('1.0',END)
        self.txt_adress.insert(END,row[11])
        file=open("user.txt","r")
        Email=file.read()
        file.close()
        if self.var_email.get()==Email:
            self.noreadonly()
        else:
            self.readonly()
        
    # def add(self):
    #     content=sqlite3.connect(database="SLMS.DataBase")
    #     cur=content.cursor()
    #     try:
    #         if self.var_roll.get()=="":
    #             messagebox.showerror("Error","Roll No. should be required",parent=self.root)
    #         else:
    #             cur.execute("select * from student1 where roll=?",(self.var_roll.get(),))
    #             row=cur.fetchone()
    #             if row!=None:
    #                 messagebox.showerror("Error","Roll No. already present",parent=self.root)
    #             else:
    #                 cur.execute("insert into student1(roll,name,email,gender,dob,contact,admission,course,state,city,pin,adress) values(?,?,?,?,?,?,?,?,?,?,?,?)",(self.var_roll.get(),self.var_name.get(),self.var_email.get(),self.var_gender.get(),self.var_dob.get(),self.var_contact.get(),self.var_a_date.get(),self.var_course.get(),self.var_state.get(),self.var_city.get(),self.var_pin.get(),self.txt_adress.get('1.0',END)))
    #                 content.commit()
    #                 messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
    #                 self.show()
    #     except Exception as ex:
    #         messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        content=sqlite3.connect(database="SLMS.DataBase")
        cur=content.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            else:
                cur.execute("select * from student1 where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","select student from list ",parent=self.root)
                else:
                    cur.execute("update student1 set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,adress=? where roll=?",(self.var_name.get(),self.var_email.get(),self.var_gender.get(),self.var_dob.get(),self.var_contact.get(),self.var_a_date.get(),self.var_course.get(),self.var_state.get(),self.var_city.get(),self.var_pin.get(),self.txt_adress.get('1.0',END),self.var_roll.get(),))
                    content.commit()
                    messagebox.showinfo("Success","Student Updated Successfully",parent=self.root)
                    if self.dash !=None:
                            self.dash.check_update()
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def show(self):
        content=sqlite3.connect(database="SLMS.DataBase")
        cur=content.cursor()
        try:
            cur.execute("select * from student1")
            rows=cur.fetchall()
            print(rows)
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def fetch_course(self):
        content=sqlite3.connect(database="SLMS.DataBase")
        cur=content.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
        
    def search(self):
        content=sqlite3.connect(database="SLMS.DataBase")
        cur=content.cursor()
        try:
            cur.execute("select * from student1 where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:
                self.course_table.delete(*self.course_table.get_children())
                self.course_table.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    


if __name__=="__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()
