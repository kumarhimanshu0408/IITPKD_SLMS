from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import subprocess

class Registration:
    def __init__(self,root):
        self.root=root
        self.root.title("REGISTRATION FORM")
        self.root.geometry("1350x700+0+0")


        #adding background image
        self.background=ImageTk.PhotoImage(file=r"C:\Users\himan\OneDrive\Desktop\1st app\abstract-red-fractal-wallpaper.jpg")
        background=Label(self.root,image=self.background).place(x=0,y=0,relwidth=1,relheight=1)


        #left image
        self.left=ImageTk.PhotoImage(file=r"C:\Users\himan\Downloads\imresizer-1685521168313.jpg")
        left=Label(self.root,image=self.left).place(x=100,y=100,width=400,height=500)


        #iit logo
        self.up=ImageTk.PhotoImage(file=r"C:\Users\himan\OneDrive\Desktop\1st app\imresizer-1685520902800.jpg")
        up=Label(self.root,image=self.up).place(x=0,y=0,width=100,height=100)
        

        #register frame
        frame1=Frame(self.root,background="white")
        frame1.place(x=480,y=100,width=750,height=500)
        
        #.....title.......
        title=Label(frame1,text="REGISTER HERE",font=("times now roman",20,"bold"),background="white",foreground="green").place(x=50,y=30)


        #.....first_name......
        f_name=Label(frame1,text="First Name",font=("times now roman",15,"bold"),background="white",foreground="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),background="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        #.....last_name....
        l_name=Label(frame1,text="Last Name",font=("times now roman",15,"bold"),background="white",foreground="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),background="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        #......contact_number.....
        contact_num=Label(frame1,text="Contact No.",font=("times now roman",15,"bold"),background="white",foreground="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),background="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        #.......email......
        email=Label(frame1,text="Enter Your Email Id",font=("times now roman",15,"bold"),background="white",foreground="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),background="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

        #......question......
        question=Label(frame1,text="Security Question",font=("times now roman",15,"bold"),background="white",foreground="gray").place(x=50,y=240)
        self.cmb_question=ttk.Combobox(frame1,font=("times now roman",13),state='readonly',justify=CENTER)
        self.cmb_question['values']=("select","What's your Pet Name","What's your School Name","What's your College Id","What's Your Nickname")
        self.cmb_question.place(x=50,y=270,width=250)
        self.cmb_question.current(0)


        #........answer.....
        answer=Label(frame1,text="Answer",font=("times now roman",15,"bold"),background="white",foreground="gray").place(x=370,y=240)
        self.txt_fanswer=Entry(frame1,font=("times new roman",15),background="lightgray")
        self.txt_fanswer.place(x=370,y=270,width=250)

        #.....password......
        password_num=Label(frame1,text="Password",font=("times now roman",15,"bold"),background="white",foreground="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),background="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

        #......current_password......
        cpassword=Label(frame1,text="Confirm Password",font=("times now roman",15,"bold"),background="white",foreground="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),background="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)
        
        #......Terms...
        self.var_check=IntVar()
        self.check=Checkbutton(frame1,text="I Agree the Terms & Conditions",variable=self.var_check,onvalue=1,offvalue=0,font=("times new roman",12),background="white").place(x=50,y=380)

        #.......signin......
        button_register=Button(frame1,text="Register Now",font=("times now roman",20),bd=0,cursor="hand2",command=self.register_data,background="#0676ad",activebackground="#0676ad").place(x=50,y=420)
        button_login=Button(self.root,text="Sign In",font=("times now roman",20),background="lightgreen",activebackground="lightgreen",command=self.signIn).place(x=200,y=520,width=180)

    def signIn(self):
        root.destroy()
        subprocess.call(["python","login.py"])
    
    
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_question.delete(0)
        self.txt_fanswer.delete(0,END)


    def register_data(self):
        content=sqlite3.connect(database="login.database")
        cur=content.cursor()
        try:
            if self.txt_fname.get()=="" or self.txt_email=="" or self.cmb_question.get()=="select" or self.txt_fanswer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" or self.txt_contact.get()=="":
                messagebox.showerror("Error","All fields Are Required",parent=self.root)
            elif self.txt_password.get()!=self.txt_cpassword.get():
                messagebox.showerror("Eroor","Password & Confirm Password Should Be Same",parent=self.root)
            elif self.var_check.get()==0:
                messagebox.showerror("Error","Please Agree our terms & conditions",parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE fname=? AND lname=?",(self.txt_fname.get(),self.txt_lname.get()))
                row=cur.fetchone()
                print("all good")
                if row !=None:
                    messagebox.showerror("Error","Student already registered",parent=self.root)
                else:
                    cur.execute("insert into student (fname,lname,email,ques,ans,password,contact) values(?,?,?,?,?,?,?)",(self.txt_fname.get(),self.txt_lname.get(),self.txt_email.get(),self.cmb_question.get(),self.txt_fanswer.get(),self.txt_password.get(),self.txt_contact.get()))
                    content.commit()

                    content1=sqlite3.connect(database="SLMS.Database")
                    cur1=content1.cursor()
                    cur1.execute("insert into student1 (name,email,contact) values(?,?,?)",(self.txt_fname.get()+" "+self.txt_lname.get(),self.txt_email.get(),self.txt_contact.get()))
                    content1.commit()

                    messagebox.showinfo("Success","Registered Successfully",parent=self.root)
                    self.clear()
                    root.destroy()
                    subprocess.call(["python","login.py"])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)


root=Tk()
object=Registration(root)
root.mainloop()
