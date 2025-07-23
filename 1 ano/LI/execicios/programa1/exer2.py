import os.path
import sys
import hashlib


#-----------------------------------------------------------------------
def compute_md5_checksum(filename, block_size=512):
    h = hashlib.md5()
    with open(filename, "rb") as f:
        while True:
            data = f.read(block_size)
            print(f"block2: {data}")
            if not data:
                break
            h.update(data)
    return h.hexdigest()
#-----------------------------------------------------------------------
mydir = os.getcwd()
print (type(mydir))
mydir=  mydir + "/"

print(f"my directory {mydir}")
print(type(sys.argv[0])) #str


filename = sys.argv[0]
filename = filename[len(mydir):]

print(filename)
h = hashlib.md5()
block_size = 512
with open(filename,"rb") as myfile:
    while True: 
        data = myfile.read(block_size)
        print(f"block1: {data}")
        if not data: #if is empty
            break
        h.update(data)

myencripion = h.hexdigest()
print(myencripion)

myencripion = compute_md5_checksum(filename,block_size)

print(myencripion)
#myfile = open(filename,"r")
#for line in myfile:
 #   print(line)
  #  h.update(line.read(512))
#
#print(h.hexdigest())
#myfile.close()
