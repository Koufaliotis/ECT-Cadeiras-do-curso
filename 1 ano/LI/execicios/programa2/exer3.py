import pytest
import sys
import os.path
from subprocess import Popen
from subprocess import PIPE

def DirectoryPaths(dir):
    myDir = os.getcwd()
    print(myDir)
    myDirfiles =os.walk(myDir)
    pathFilesLst = []
    for files in myDirfiles:
        data = files[2]
        for file in data:
            pathFilesLst.append(myDir + f"/{file}")

#print(pathFilesLst)
    if dir in pathFilesLst:
        FileData(dir)
    else:
        print("the file directory is not valid")
    

#get file dir and verify 
#print(sys.argv[0])

def FileData(dir):
    proc = Popen(f"ls -la {dir}" , stdout=PIPE, shell=True) #proc = Popen(f"ls -la {sys.argv[0]}" , stdout=PIPE, shell=True)
    return_code = proc.wait()
    output = proc.stdout.read().decode("utf-8")#? returns info of the files
    print(output, return_code)
    return output,return_code