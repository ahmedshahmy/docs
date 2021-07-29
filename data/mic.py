#!/usr/bin/env python3
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time as tm

duration = 10 #in seconds
y=0

x=1


def audio_callback(indata, frames, time, status):
   
   volume_norm = np.linalg.norm(indata) * 1000000
   print(int(volume_norm))
   y=int(volume_norm)
   frames+=1
   plt.scatter(time.strftime("%H:%M:%S", tm.localtime()), y)
   plt.pause(0.1)
   plt.draw()


stream = sd.InputStream(callback=audio_callback)

with stream:
   sd.sleep(duration * 1000)


   