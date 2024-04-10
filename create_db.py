import sqlite3 
def create_db():
    con=sqlite3.connect(database=r'ics.db')
    cur=con.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,name text,price text,qty text,status text)")
    con.commit()

    
    
create_db()