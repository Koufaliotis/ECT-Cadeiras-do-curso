#cifraComRC4
import os.path
from Cryptodome.Cipher import ARC4

def dicyfer(cryptogram,mykey):
    
    deChifer = ARC4.new(mykey.encode("utf-8"))
    finalStep= deChifer.decrypt(cryptogram)
    print(finalStep.decode("utf-8"))



myDir = os.getcwd()
filesInDir = os.walk(myDir)
print(filesInDir)

key = input("give a word to make key: ")
if len(key) < 5:
    import hashlib
    myHash = hashlib.sha256()
    myHash.update(key.encode("utf-8"))
    mykey = myHash.hexdigest()
    print(mykey)

elif len(key) >= 256:
    mykey = key
else:
    mykey = key[:256]


chifer =ARC4.new(mykey.encode("utf-8"))

for dirData in filesInDir:
    print(dirData)
    files = dirData[2]
    file = files[4]
    with open(file,"r") as myFile:
        while True:
            data = myFile.read(256)
            if not data:
                break
            print(type(data))
            cryptogram = chifer.encrypt(data.encode("utf-8"))

           
        print(cryptogram)
        print(os.write(1, cryptogram)) #what is this?
        myCryptogram = cryptogram
        #myCryptogram = os.write(1, cryptogram)


with open("cripotograma.txt", "w") as myFile1:
    myFile1.write(str(myCryptogram))
    print()
    print(myCryptogram)
    print(mykey)
dicyfer(myCryptogram,mykey)




#myFile1 = open("cripotograma.txt","wb")
#for line in myFile1:
 #   line.write(myCryptogram)
#
#
#myFile1.close()







#key ="Marcos"
#chifer = ARC4.new(key.encode("utf-8"))
#text = "agh"
#criptograma = chifer.encrypt("awerg".encode)