import hashlib
from Cryptodome.Cipher import ARC4
import os.path

myDir = os.getcwd()

filesInDir = os.walk(myDir)

for myfiles in filesInDir:
    print(myfiles)
    myFile = myfiles[2][4]


key = input("give me a key: ")
myCyfer = ARC4.new(key.encode("utf-8"))

with open(myFile,"r") as fileData:
    Data = fileData.read()
    print(Data)
    print()
    myCryptogram = myCyfer.encrypt(Data.encode("utf-8"))
    
print(myCryptogram)

myDecyfer = ARC4.new(key.encode("utf-8"))
myDecription = myDecyfer.decrypt(myCryptogram)
Decripted = myDecription.decode("utf-8")
print()
print(Decripted) 





