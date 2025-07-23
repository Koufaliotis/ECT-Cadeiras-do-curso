import csv
import random
import math
valuelst =[]
line = 1
with open("csvTest.txt","r") as myfile:
    csvReader = csv.reader(myfile,delimiter=",")
    next(csvReader)
    for fileData in csvReader:
        
        print(fileData)
        if line != 3:
            value = fileData[3]
            valuelst.append(float(value[-4:-1]))
        line += 1

##minimo
print("minimo")
print (min(valuelst))

print("maximo")
print (max(valuelst))

print("media")
print ((valuelst[0] +valuelst[1]+ valuelst[2])/len(valuelst))