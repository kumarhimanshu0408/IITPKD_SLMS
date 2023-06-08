from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import subprocess

root=Tk()
root.title("Login")
root.geometry('1200x700')



back=Image.open("IMG-20230601-WA0000-01.jpeg.jpg")
back=back.resize((1200,700))


background=ImageTk.PhotoImage(back)
background_label = Label(root,image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


login_frame=Frame(root,bg='#804000')
login_frame.place(relx=0.5, rely=0.5, anchor=CENTER,height=400,width=700)

Label(login_frame,text="FORGOT PASSWORD!!",font=("times new roman",24,"bold"),bg="#804000",fg="lightblue").place(x=280,y=30)



Email_label=Label(login_frame,text="Email    :",font=("times new roman",18,"bold"),bg="#804000")
Email_label.place(x=300,y=80)
question=Label(login_frame,text="Security Question :",bg="#804000",font=("times now roman",15,"bold")).place(x=300,y=140)
cmb_question=ttk.Combobox(login_frame,background="#ffe6cc",font=("times now roman",13),state='readonly',justify=CENTER)
cmb_question['values']=("select","What's your Pet Name","What's your School Name","What's your College Id","What's Your Nickname")
cmb_question.place(x=300,y=170,width=250)
cmb_question.current(0)

answer_label=Label(login_frame,text="Answer :",font=("times new roman",18,"bold"),bg="#804000")
answer_label.place(x=300,y=200)

Email=Entry(login_frame,font=("times new roman",18,"bold"),bg="#ffe6cc")
Email.place(x=300,y=110)

answer=Entry(login_frame,font=("times new roman",18,"bold"),bg="#ffe6cc")
answer.place(x=300,y=230)

password_label=Label(login_frame,text="Password",font=("times new roman",18,"bold"),bg="#804000")
password_label.place(x=300,y=260)

password=Entry(login_frame,font=("times new roman",18,"bold"),bg="#ffe6cc",show="*")
password.place(x=300,y=290)

def submit():
    content=sqlite3.connect(database="login.database")
    cur=content.cursor()
    try:
        if Email=="" or question=="" or answer=="" or password =="":
            messagebox.showerror("Error","All fields Are Required",parent=root)
        else:
            cur.execute("SELECT * FROM student WHERE email=?",(Email.get(),))
            row=cur.fetchone()
            print("all good")
            if row ==None:
                messagebox.showerror("Error","Student not registered",parent=root)
            else:
                if row[4] !=cmb_question.get() or row[5] !=answer.get() :
                    messagebox.showerror("Error","Wrong answer or question",parent=root)
                else:
                    cur.execute("insert into student (password) values(?)",(password.get(),))
                    messagebox.showinfo("Success","Registered Successfully",parent=root)
                    root.destroy()
                    subprocess.call(["python","login.py"])
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}",parent=root)

    


submit_btn=Button(login_frame,text="Change Password",font=("times new roman",14,"normal"),command=submit,bg="#006600")
submit_btn.place(x=370,y=340)

img=Image.open("APJ2.jpg")
img=img.resize((330,350))
welcome=ImageTk.PhotoImage(img)
wel_frame=Frame(root,bg="black")
wel_frame.place(x=200,y=176,height=350,width=320)
welcome_label = Label(wel_frame,image=welcome,padx=20,pady=20)
welcome_label.place(x=0,y=0)



root.mainloop()
