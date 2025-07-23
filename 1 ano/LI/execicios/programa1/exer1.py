import os.path
import sys
import os
import hashlib
print("sys.argv[0]:", sys.argv[0])
print("python 3 %s")
#---------------------------
mydir = os.getcwd()
print (type(mydir))
mydir=  mydir + "/"

print(f"my directory {mydir}")
print(type(sys.argv[0])) #str


filename = sys.argv[0]
filename = filename[len(mydir):]
print(filename)
h = hashlib.md5()
myfile = open(filename,"r")
for line in myfile:
    print(line)
    h.update(line.encode("utf-8"))

print(h.hexdigest())
#--------------------------------------
myfile.close()

if len(sys.argv) < 2:
    print ("Usage: python3 %s filename" % (sys.argv[0]))#does not print argv[0]?
    sys.exit(1)



