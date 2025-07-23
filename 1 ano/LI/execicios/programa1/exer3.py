import hashlib
import os.path
import Cryptodome
import sys
from Cryptodome.Hash import SHA256

myDir = os.getcwd()
print(myDir)

#print(help(sys)) #q to exit
#for i in myDir:
filedir = os.walk(myDir)
print(filedir)
myfiles = []
print(type(myfiles))
for dirData in filedir:
    print(dirData)
    for file in dirData[2]:
        myfiles.append(file)
print(myfiles)

#myhush = hashlib.md5()
myhush = hashlib.sha256()
blockSize = 256

for file in myfiles:
    with open(file,"rb") as myfile:
        while True:

            data = myfile.read()
            print(f"block: {data}")
            if not data:
                break
            myhush.update(data)

print(myhush.hexdigest())

        


