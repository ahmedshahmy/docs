#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Dec 01, 2020 11:07:32 AM +0530  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import pyrebase
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from datetime import datetime
import numpy as np

firebasConfig={
    'apiKey': "AIzaSyAyOKsYNnwrxwgmMy-7qQsT7QiYIcWF3-I",
    'authDomain': "renal-1e0ac.firebaseapp.com",
    'databaseURL': "https://renal-1e0ac.firebaseio.com",
    'projectId': "renal-1e0ac",
    'storageBucket': "renal-1e0ac.appspot.com",
    'messagingSenderId': "39709818947",
    'appId': "1:39709818947:web:8998d016a6d9e4ffa854f6",
    'measurementId': "G-1R80GQM1G8"
}

firebase=pyrebase.initialize_app(firebasConfig)
db=firebase.database()

#global x
#global y

global x1
global y1
x1=[]
y1=[]

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def add(name,date,creat):
    date=date+"  "
    data={"RU":name,"date":date,"Creatinine":creat}
    db.child("patients1").push(data)
    print('renal1_support.add')
    sys.stdout.flush()

def graph(name):
    x=[]
    y=[]
    patients=db.child("patients1").order_by_child("RU").equal_to(name).get()

    for p in patients.each():
    
    
    #print(p.val()["date"])
        try:

            y.append(float(p.val()["Creatinine"]))
            x.append(datetime.strptime(p.val()["date"],'%m/%d/%Y  '))
        except Exception as e:
            print(e)
            continue

            


    

    plt.scatter(x, y)
    #plt.plot(x,y)
    print(x,y)
    plt.yticks(y)

    
    
    #plt.plot(x,y)
    plt.yscale('log')
    plt.gca().invert_yaxis()
    plt.xticks(x)
    plt.yticks(y)

    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
    ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())

    plt.xlabel("date")
    plt.ylabel("-log. S.Cr")
    plt.xticks(rotation=70)
    mng = plt.get_current_fig_manager()
    mng.resize(1000,1000)
    plt.show()

    print('renal1_support.graph')
    sys.stdout.flush()


"""
    i=100

    while i<1000:
        plt.axhline(y=i,color='grey')
        i+=100
"""
    #plt.axhline(y=500,color='red', label='500')
    #plt.legend()
    
    #plt.yticks([100,200,300,400,500,600,700,800,900,1000])
    

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import renal1
    renal1.vp_start_gui()




