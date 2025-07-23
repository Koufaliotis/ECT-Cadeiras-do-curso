import sys
import hashlib
from Cryptodome.Cipher import ARC4

import hashlib
from Cryptodome.Cipher import ARC4
import os.path

myDir = os.getcwd()

filesInDir = os.walk(myDir)

for myfiles in filesInDir:
    print(myfiles)
    myFile = myfiles[2][4]


key = input("give me a key: ")

#---------------------------------------
if len(key) < 5:
    import hashlib
    myHash = hashlib.sha256()
    myHash.update(key.encode("utf-8"))
    mykey = myHash.hexdigest()
    print(mykey)

elif len(key) <= 256:
    mykey = key
else:
    mykey = key[:256]

#---------------------------------------

myCyfer = ARC4.new(mykey.encode("utf-8")) #alt key

with open(myFile,"r") as fileData:
    Data = fileData.read()
    print(Data)
    print()
    myCryptogram = myCyfer.encrypt(Data.encode("utf-8"))
    
print(myCryptogram)

myDecyfer = ARC4.new(mykey.encode("utf-8")) #alt key
myDecription = myDecyfer.decrypt(myCryptogram)
Decripted = myDecription.decode("utf-8")
print()
print(Decripted) 