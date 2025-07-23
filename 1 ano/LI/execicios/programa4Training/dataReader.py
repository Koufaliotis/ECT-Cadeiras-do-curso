import csv
import random
import psutil
import time
import json
from xml import etree
def Reader(file,separetor):
    #separetor: "," or ";" or"|"
    dic ={}
    myfile = open(file,"r")

    for line in myfile:
        data = line.split(separetor)
        print( data[0]+" : "+data[1]+" : "+data[2]+" : "+data[3])
        tempraturas.append(data[3])
    myfile.close()

def TemperaturaMedia():
    sum = 0
    for i in tempraturas:
        sum += i
    return sum/len(tempraturas)
tempraturas = []

def cvsReader(f):
    myfile = open(f,"r")
    data = csv.reader(myfile,delimiter =",")
    for row in data:
        print(row)
    
    myfile.close()

def csv_Writer(f):
    myfile = open(f,"w")
    writer = csv.DictWriter(myfile,["time","value"])
    
    writer.writeheader() # writes "time" and "value"
    for row in range(1,10):
        writer.writerow({"time": row, "value" : random.randint(1,100)})
    myfile.close()

def psutilTest():
    freq = psutil.cpu_freq()
    usage = psutil.cpu_percent()
    stats =psutil.cpu_stats()

    print(freq,usage,stats)

    print(time.time())
    
    print(time.localtime())

def jsonEditor():
    #data = [{"time" : 213,"name": "cpu", "value" : 12},
     #       {"time" : 785,"name": "cpu", "value" : 24}

    #]
    data = [{"stats":[
        {"time" : 213,"name": "cpu", "value" : 12},
        {"time" : 785,"name": "cpu", "value" : 24}
    ]}]
    print(json.dumps(data,indent = 6))
    print(json.dumps(data))



#psutilTest()
#cvsReader("cvs.txt")
#csv_Writer("cvs.txt")
jsonEditor()
