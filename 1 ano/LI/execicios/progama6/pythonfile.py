import sqlite3 as sql
import os.path
#myDB = sql.connect("/home/marcos/Desktop/infurmatica/LD/exercicios/progama6/companies2.db")

def test1():
    print("\n")
    db = sql.connect('/home/marcos/Desktop/infurmatica/LD/exercicios/progama6/companies2.db')
    result2 = db.execute("SELECT * FROM contacts")
    rows2 = result2.fetchone() # returns only the firstone
    for row2 in rows2:
        print(row2)

    #while True:
     #   rows2 = result2.fetchone()#????
      #  if not rows2:
       #     break
        #print(rows2)
    db.close()

def Interact():
    db = sql.connect('/home/marcos/Desktop/infurmatica/LD/exercicios/progama6/companies2.db')    
    myComand = input("first name: ")
    result3 = db.execute("SELECT * FROM contacts WHERE firstname LIKE ?",(myComand,))
    print(result3)
    data =result3.fetchall

    for dat in data:
        print(dat)
    db.close()
mydir = os.getcwd()
print(mydir)

print(os.walk(mydir))
myFiles = os.walk(mydir)

for files in myFiles:
    print(files)
    File = files[2][1]
print(File)
print("\n")
myDB = sql.connect('/home/marcos/Desktop/infurmatica/LD/exercicios/progama6/companies2.db')
#myDB = sql.connect(File)
result =myDB.execute("SELECT * FROM contacts")
print(result)
rows = result.fetchall()
print(rows)
print("\n")

for row in rows:
    print(row)
    


myDB.close()
#test1()
Interact()

