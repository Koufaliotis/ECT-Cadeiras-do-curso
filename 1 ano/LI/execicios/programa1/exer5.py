#cifraComAES.py 1.8
from Cryptodome.Cipher import AES
import os.path


key = input("give me a key: ")
while True:
    
    if len(key) < 16:
        
    # form sha256 16 char
        import hashlib    
        myhash =hashlib.sha256()
        myhash.update(key.encode("utf-8"))
        mykey = myhash.hexdigest()
        mykey = mykey[0:16]
        print(mykey)
        break
    elif len(key) == 16 or len(key) == 24 or len(key) == 32:
        mykey = key
        break
    else:
        print("the key must have 16 or 24 or 32 or less than 16 char")
cipher = AES.new(mykey.encode("utf-8"), AES.MODE_ECB)
criptogram = cipher.encrypt("texto para cifra".encode("utf-8"))
print(criptogram)
print(os.write(1,criptogram))

mydir = os.getcwd()
myFolder = os.walk(mydir)
for files in myFolder:
    
    myFiles = files[2]
    print(myFiles)