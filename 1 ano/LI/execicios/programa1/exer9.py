import os.path
from Cryptodome.Cipher import AES
mydir = os.getcwd()
files = os.walk(mydir)

for myfiles in files:
    myfile = myfiles[2]
    print(myfile)

#cipher the file

with open(myfile[4],"r") as fileData:
    data = fileData.read()
    print(type(data))
    key ="0123456789abcdef"
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
    criptogram = cipher.encrypt("adghhfjfvxcv".encode("utf-8"))
    print(criptogram)

print(os.path.getsize("cripotograma.txt"))