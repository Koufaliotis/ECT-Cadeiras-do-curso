import sqlite3
import sys
import os.path

def ProcessData(file):
    db = sqlite3.connect(file)
    print(db) #cant acess with for
    #tables = db.execute(".tables") #doesnt work
    tableData = db.execute("SELECT * FROM contacts")
    for data in tableData: #it can remove a row if used
        print(data)#prints tuples
    print("---------------------------------------------------------------")
    tableData = db.execute("SELECT * FROM contacts")
    while True:
        row = tableData.fetchone()
        if not row:
            break
        print(row)
    print("---------------------------------------------------------------")    
    endMail = input("select the end of a email like gmail.com: ")
    result = db.execute("SELECT * FROM contacts WHERE email LIKE ?",("%"+ endMail,))
    #print(result)
    for data in result:
        print(data)
    db.close()

    #create a new database
    
#----------------------------------------
myDir = os.getcwd() #os.mkdir()
print(myDir)

files = os.walk(myDir)
for file in files: 
    print(file)
    myfiles  = file[2]

print(myfiles)
myfile = myfiles[1]

ProcessData(myfile)