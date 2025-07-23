import csv
import random


fout = open("randomNum.csv","w")
writer = csv.DictWriter(fout, fieldnames = ["time","value"]) ##file slots
writer.writeheader()#??? its like a constractor of the file slots after the file definition
for i in range(1,10):
    writer.writerow({"time" : i,"value" : random.randint(1,100)})
