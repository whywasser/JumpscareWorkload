#import modules
import systole
from systole.recording import Oximeter
from systole import serialSim
import serial
import keyboard
import numpy
import time
import os

print("Please enter ParticipantID:")
ParticipantID = input()
print("Please enter condition:")
condition = input()
folderpath = "C:\Users\Apexo\Desktop\PPGData\" + ParticipantID 
os.mkdir(folderpath)
ser = serialSim()
#ser = serial.Serial("COM4")
oxi = Oximeter(serial=ser).setup()
timelist = []
duration = 60
tstart = time.time()
number = 1
try:
    while True:
        oxi.readInWaiting()
        if time.time()-tstart>duration:
            filename = folderpath + "/" + condition + str(number) + ".npy"
            print(filename)
            oxi.save(filename)
            timelist.append(str(time.time()))
            oxi.reset(serial=ser)
            tstart = time.time()
            number = number+1
            print(timelist)
except KeyboardInterrupt:
    print("done")
