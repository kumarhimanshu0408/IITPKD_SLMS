import pyttsx3
import speech_recognition as sr
import datetime
import sqlite3
import time as tt

good=True

def close():
    global good
    print("from voice")
    good=False
    print(good)

def speech_to_text():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data

        except sr.UnknownValueError:
            print(text_to_speech("Didn't Understand!! Can You Speak Again..."))

def text_to_speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',120)
    engine.say(x)
    engine.runAndWait()

def isgood():
    print(good)
    return good


def voiceAssist(t):
    global good
    print("reached here")
    requestleave=False
    while True:
          if not isgood():
               print("reeeech")
               return False
          t.config(bg="green")
          data1=str(speech_to_text()).lower()
          t.config(bg="red")
          if " no " in data1:
               text_to_speech("I am soory for that..")
          if "your name" in data1 or "hello" in data1:
               name = "Hey, This Is GyaAAni.\n how may I assist you "
               text_to_speech(name)

          elif "register" in data1 or "registration" in data1:
               age = "GO TO login page and click sign up. Then fill up the details and accept our terms and conditions.Click on register. You will be taken to the login page. Sign in into your newly made account "
               text_to_speech(age)

          elif "add" in data1:
               if "student" in data1:
                    nme = "Click on the student button in the dashboard.\n then fill all the empty fields and click save."
               elif "course" in data1:
                    nme="Clcik on the courses button in the dashboard. \n then fill all the required sections and click save."
               elif "result" in data1:
                    nme="Click on the result button in the dashboard. \n then fill all the required data according to your course and click on submit button. "
               text_to_speech(nme)

          elif "remove" in data1 or "delete" in data1:
               if "course" in data1:
                    nm = "Go to the course section from the dashboard .\n then click the course to delete.\n Now click the 'delete' button ." 
               elif "student" in data1:
                    nm="Soory you cannot delete any student other than you"
               text_to_speech(nm)
          elif "check" in data1 or "view" in data1:
               if "result" in data1:
                    bnm="click on the view result button and type your roll number\n and select any one of the courses and tap on the show result."
               else:
                    bnm="You can only check for result"
               text_to_speech(bnm)

          elif "time" in data1:
               time = datetime.datetime.now().strftime("%I%M%p")
               text_to_speech(time)

          elif "current user" in data1:
               file=open("user.txt","r")
               Email=file.read()
               file.close()   
               content=sqlite3.connect(database="SLMS.DataBase")
               cur=content.cursor()
               cur.execute("select name from student1 where email=?",(Email,))
               row=cur.fetchone()
               strr="You are logged in as "+row[0]
               text_to_speech(strr)
          elif "open" in data1 or "go to" in data1:
               if "course" in data1:
                    return "course"
               elif "student" in data1:
                    return "student"
               elif "result" in data1:
                    return "result"
               elif "view result" in data1:
                    return "vresult"
          elif "exit" in data1 and "app" in data1:
               text_to_speech("Thank You, Have a Nice Day!!")
               return "exit"

          elif "exit" in data1 or not isgood():
               text_to_speech("Thank You, Have a Nice Day!!")
               good=True
               return False
          else:
               text_to_speech("Sorry. Can't answer that. I think my developers forgot to include it in my code")
          tt.sleep(1)
               
               


     
