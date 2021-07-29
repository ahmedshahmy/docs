import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


import serial
import time

serialPort = serial.Serial(
    port="COM5", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)
serialString = ""  # Used to hold data coming over UART
while 1:
    # Wait until there is data waiting in the serial buffer
    if serialPort.in_waiting > 0:

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        try:
            print(serialString.decode("Ascii"))
        except:
            pass
        
global x
global y
x=[]
y=[]
with open('ct.csv') as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    xx=1
    for row in readCSV:
        x.append(xx)
        y.append(int(row[1]))
        xx+=1


#plt.xticks=x[:100]
#plt.yticks=y[:100]



#plt.subplots_adjust(bottom=0.25)

#t = np.arange(0.0, 100.0, 0.1)
#s = np.sin(2*np.pi*t)
#plt.axis([0, 10, 0, 1])

#for i in range(100):
   
#    plt.scatter(i, y[i])
#    plt.pause(0.1)
    #plt.draw()
#plt.plot(x,y)

for t in x:
    #print(t)
    if(t%500==0):
        g=int(t/500)
        xf=(g-1)*500
        xt=g*500

        plt.plot(x[xf:xt],y[xf:xt])
        g=str(t/500)
        plt.savefig("ecg/img"+g+".png")
        print("image"+g+"saved")
        plt.clf()


plt.show()
#print(y)
#plt.axis([0, 10, -1, 1])



#plt.show()