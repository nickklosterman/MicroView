#!/usr/bin/env python
import sys
import time
import serial
import time
PORT = "/dev/ttyUSB1"

TIMEFORMAT = "%m/%d/%y %H:%M:%S"
INTERVAL = 0.21
x = 0
TFLN = []

def readTFLN():
    if ( len(sys.argv) >= 1 ):
        fileHandle=open(sys.argv[1],'r')
        #there is a better way to read in the contents...
        for line in fileHandle:
            TFLN.append(line)
    else:
        print("Enter a file to be read in")
        print(sys.argv[1])
        sys.exit(1)

def getTimeList():
    statFile = file("/proc/stat", "r")
    timeList = statFile.readline().split(" ")[2:6]
    statFile.close()
    for i in range(len(timeList))  :
        timeList[i] = int(timeList[i])
    return timeList

def deltaTime(interval)  :
    x = getTimeList()
    time.sleep(interval)
    y = getTimeList()
    for i in range(len(x))  :
        y[i] -= x[i]
    return y

if __name__ == "__main__"  :
	args = sys.argv
        readTFLN()
        tempString = ""
while True :
        #dt = deltaTime(INTERVAL)
    time.sleep(INTERVAL)
        #timeStamp = time.strftime(TIMEFORMAT)
        #cpuPct = 100 - (dt[len(dt) - 1] * 100.00 / sum(dt))
        
    while len(tempString) < 50:
        tempString+=TFLN[x]
        x+=1
        y=0
        
    outputString=tempString[y:]
    outputString+=" "
    if len(outputString.strip()) < 1:
        tempString=""
    try:
        ser = serial.Serial(PORT,9600)
		#ser.write(str('%.4f' %cpuPct))
        ser.write(outputString) #bob)
        if y == 0:
            time.sleep(1.5)
        #ser.write('\n')
                #print(('%.4f' %cpuPct))
                #print(bob)
        print(outputString)
    except:
        print str("NO USB DEVICE CONECTED TO " + PORT)
    y+=1
    print(y)
    print(outputString)
                
