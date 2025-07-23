import hashlib
import os.path
from Cryptodome.Cipher import ARC4
import Cryptodome.Hash
from Cryptodome.Cipher import AES

def training1():
    h = hashlib.md5()
    h.update("asdfasdfasfd".encode("utf-8"))
    print(h.hexdigest())

    myhash = hashlib.md5()
    mymesage = input("message: ")
    myhash.update(mymesage.encode("utf-8"))
    print(myhash.hexdigest())

#training1()

def exer1():
    mydir = os.getcwd()
    print(mydir)
    filesInDir = os.walk(mydir)
    for dirData in filesInDir:
        print(dirData)
        myfiles = dirData[2]

    print(myfiles)
    myhash = hashlib.sha1()
    with open(myfiles[5],"rb") as myfile:
        while True:
            print(f"block: {myfile.read(512)}")
            mymessage = myfile.read(512)
            if not mymessage:
                break
            myhash.update(mymessage.encode("utf-8"))

    print(myhash.hexdigest())
#da39a3ee5e6b4b0d3255bfef95601890afd80709
#exer1()

def training2():
    #doesnt work
    return


#training2()

def exer3():
    mydir = os.getcwd()
    print(mydir)
    filesInDir = os.walk(mydir)
    for dirData in filesInDir:
        print(dirData)
        myfiles = dirData[2]
    
    print(myfiles)
    
    myhash256 = hashlib.sha256()
    
    with open(myfiles[5],"r") as myfile:
        while True:
            mymessage = myfile.read(256)
            if not mymessage:
                break
            myhash256.update(mymessage.encode("utf-8"))
    print(myhash256.hexdigest())
#exer3()

def training3():
    myDir = os.getcwd() 
    myDirFiles = os.walk(myDir)
    for myFiles in myDirFiles:
        files =myFiles[2]
    myfiles = files[5]
    print(myfiles)
    
    key = input("give me a key: ")
    chiper = ARC4.new(key.encode("utf-8"))
    
    criptogram = chiper.encrypt(input("encreapt message: ").encode("utf-8"))

    decipher = ARC4.new(key.encode("utf-8"))
    decrypt = decipher.decrypt(criptogram)

    print(decrypt.decode("utf-8"))    
#training3()

def testingAES():
    key = "0123456789abcdef"
    cypher = AES.new(key.encode("utf-8"), AES.MODE_ECB)
    
    
    x = cypher.encrypt("my message asdfa".encode("utf-8")) #must a have a limited num o car 16 or 32 or 64 ...
    print(x)


testingAES()
    
#x = cypher.encrypt("texto para cifra".encode("utf-8"))