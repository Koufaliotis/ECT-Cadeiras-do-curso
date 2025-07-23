import os.path
import wave
import pyaudio
import math
from struct import pack #????????????????????????????????????????????

def exer1(file):
    wf = wave.open("wave_files/" + file,"rb")
    print(wf.getnchannels())

    wf.close()

def audioPlayer(file):
    wf = wave.open("wave_files/" + file,"rb")
    player = pyaudio.PyAudio()

    stream = player.open(format = player.get_format_from_width(wf.getsampwidth()),channels = wf.getnchannels(),rate = wf.getframerate(), output = True)

    while True:
        data = wf.readframes(1024)
        if not data:
            break
        stream.write(data)
    stream.close()
    player.terminate()
    wf.close()

def audioPlayerEditor(rate2):
    wf = wave.open("wave_files/piano-c5-c6.wav","rb")
    print(wf.getframerate())
    player = pyaudio.PyAudio()

    stream = player.open(format = player.get_format_from_width(wf.getsampwidth()),channels = wf.getnchannels(),rate = rate2, output = True)

    while True:
        data = wf.readframes(1024)
        if not data:
            break
        stream.write(data)
    stream.close()
    player.terminate()
    wf.close()

def exer4():
    rate=44100
    wv = wave.open("wave_files/laught.wav", "w")
    wv.setparams((1, 2, rate, 0, "NONE", "not compressed"))
    amplitude = 10000
    data = []
    freq = 440
    duration = 1 # Em segundos
    for i in range(0, rate * duration):
        data.append(amplitude*math.sin(2*math.pi*freq*i/rate))
        # Gerar (pack) a informação no formato correto (16bits)
        wvData = []
        for v in data:
            if v >= 0:
                wvData += pack("h", int(v))
            else:
                v=v*(-1)
                wvData += pack("h", int(v))
                wv.writeframes(bytearray(wvData))
    wv.close()

#----------------------------------------------------------
myDir = os.getcwd()
print(myDir)

myfiles = os.walk(myDir)
for data in myfiles:
    print(data)
    files = data[2]
for file in files: 
    #exer1(file)
    print("the "+file+" is playing\n")
    #audioPlayer(file)

#for rate in [20000,34000,44100,120000]:
 #   print(rate)
    #audioPlayerEditor(rate)

exer4()