import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import subprocess
import sqlite3


if __name__=="__main__":
    root=tk.Tk()
    root.title("Login")
    root.geometry('1200x700')


    back=Image.open("IMG-20230601-WA0000-01.jpeg.jpg")
    back=back.resize((1200,700))


    background=ImageTk.PhotoImage(back)
    background_label = tk.Label(root,image=background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    login_frame=tk.Frame(root,bg='#804000')
    login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER,height=400,width=700)



    Email_label=tk.Label(login_frame,text="Email    :",font=("times new roman",18,"bold"),bg="#804000")
    Email_label.place(x=300,y=100)
    Password_label=tk.Label(login_frame,text="Password :",font=("times new roman",18,"bold"),bg="#804000")
    Password_label.place(x=300,y=160)

    Email=tk.Entry(login_frame,font=("times new roman",18,"bold"),bg="#ffe6cc")
    Email.place(x=300,y=130)
    print(Email)

    Password=tk.Entry(login_frame,font=("times new roman",18,"bold"),bg="#ffe6cc",show="*")
    Password.place(x=300,y=190)

    def submit():
        global Email,Password,root

        content=sqlite3.connect(database="login.database")
        cur=content.cursor()
        try:
            if Email.get()=="" or Password.get()=="":
                messagebox.showerror("Error","All fields Are Required",parent=root)
            else:
                cur.execute("SELECT * FROM student WHERE email=?",(Email.get(),))
                row=cur.fetchone()
                if row ==None:
                    messagebox.showerror("Error","Student Not registered",parent=root)
                else:
                    cur.execute("SELECT * FROM student WHERE password=?",(Password.get(),))
                    row2=cur.fetchone()
                    if row2==None:
                        messagebox.showerror("Login","Wrong Password.Try Again.",parent=root)
                    else:
                        file=open("user.txt","w")
                        print(Email.get(),file=file,end="")
                        file.close()

                        root.destroy()
                        subprocess.call(["python","SLMS_dashboard.py"])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=root)

    def submit1():
        root.destroy()
        subprocess.call(["python","forget.py"])

    def submit2():
        root.destroy() 
        subprocess.call(["python","SLMS_registerwin.py"])


    submit_btn=tk.Button(login_frame,text="LOGIN",font=("times new roman",14,"normal"),command=submit,bg="#006600")
    submit_btn.place(x=370,y=250)

    img=Image.open("APJ2.jpg")
    img=img.resize((330,350))
    welcome=ImageTk.PhotoImage(img)
    wel_frame=tk.Frame(root,bg="black")
    wel_frame.place(x=200,y=176,height=350,width=320)
    welcome_label = tk.Label(wel_frame,image=welcome,padx=20,pady=20)
    welcome_label.place(x=0,y=0)

    forget_pass=tk.Button(login_frame,bd=0,bg="#804000",fg="#eee6ff",text="Forget Password",font=("times new roman",10,"normal"),command=submit1)
    forget_pass.place(x=300,y=320)
    forget_pass.configure(cursor="hand2")

    forget_pass=tk.Button(login_frame,bd=0,bg="#804000",fg="#eee6ff",text="Sign Up..",font=("times new roman",10,"normal"),command=submit2)
    forget_pass.place(x=470,y=320)
    forget_pass.configure(cursor="hand2")



    root.mainloop()
