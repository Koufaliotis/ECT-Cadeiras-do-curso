import psutil
import time
import json

def jsonAdd(pctime,cpuName,Cpu):
    data =[
        {   "datalist" :[ 
                {"time": pctime, "name": cpuName, "value": Cpu}
                
                
                ]
        }
    ]
    print(json.dumps(data, indent=4))


start_time = time.time()

print(psutil.cpu_freq())

while True :
    pcTime = int(time.time() - start_time)
    cpu = psutil.cpu_percent(interval=1)
    #CpuFreq = psutil.cpu_freq()
    jsonAdd(pcTime,"mycpu",cpu)
    
    if pcTime >= 60:
        break