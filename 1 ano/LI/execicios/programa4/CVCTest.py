import sys
import csv
import random
def main(argv):
    fich_csv = open("csvTest.txt", "r")
    csv_reader = csv.reader(fich_csv, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        print(row)
    fich_csv.close()

#main(sys.argv)

def main2():
    fout = open("rand.csv", "w")
    writer = csv.DictWriter(fout, fieldnames=["time", "value"])
    writer.writeheader()
    for i in range(1,10):
        writer.writerow({"time": i, "value" : random.randint(1,100)} )
    fout.close()
main2()