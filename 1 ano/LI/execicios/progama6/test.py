import sqlite3 as sql
import os

mydir = os.getcwd()
print("Current directory:", mydir)

# Get all files in the current directory
myFiles = os.walk(mydir)

File = None
for root, dirs, files in myFiles:
    for filename in files:
        if filename.endswith(".db"):  # Look for a database file
            File = os.path.join(root, filename)
            break

if File:
    print("Using database file:", File)
    try:
        myDB = sql.connect(File)
        result = myDB.execute("SELECT * FROM companies2;")

        print("\nDatabase Contents:")
        for row in result:
            print(row)

        myDB.close()
    except sql.Error as e:
        print("Database error:", e)
else:
    print("No .db file found in the directory.")