import sqlite3
def create_db():
    content=sqlite3.connect(database="SLMS.DataBase")
    cur=content.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,charges text,description text,studentemail text)")
    content.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student1(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,adress text)")
    content.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,course text,marksobtained text,fullmarks text,percent text)")
    content.commit()


    content.close()

    content1=sqlite3.connect(database="login.database")
    cur1=content1.cursor()
    cur1.execute("CREATE TABLE IF NOT EXISTS student(cid INTEGER PRIMARY KEY AUTOINCREMENT,fname text,lname text,email text,ques text,ans text,password text,contact text)")
    content1.commit()

    content1.close()

    
create_db()