 #! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Dec 08, 2020 07:57:36 AM +0530  platform: Linux

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

import add_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    add_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    add_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("683x532+650+202")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.title("CKD Progression Analyzer-Register Patient .beta. maa.shahmy@gmail.com")

        self.EntryRU = tk.Entry(top)
        self.EntryRU.place(relx=0.501, rely=0.267, height=33, relwidth=0.243)
        self.EntryRU.configure(background="white")
        self.EntryRU.configure(font="TkFixedFont")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.278, rely=0.282, height=25, width=44)
        self.Label1.configure(text='''RU''')

        self.EntryName = tk.Entry(top)
        self.EntryName.place(relx=0.501, rely=0.423, height=33, relwidth=0.243)
        self.EntryName.configure(background="white")
        self.EntryName.configure(font="TkFixedFont")

        self.EntryAge = tk.Entry(top)
        self.EntryAge.place(relx=0.501, rely=0.577, height=33, relwidth=0.243)
        self.EntryAge.configure(background="white")
        self.EntryAge.configure(font="TkFixedFont")

        self.EntrySex = tk.Entry(top)
        self.EntrySex.place(relx=0.501, rely=0.733, height=33, relwidth=0.243)
        self.EntrySex.configure(background="white")
        self.EntrySex.configure(font="TkFixedFont")

        self.ButtonAdd = tk.Button(top)
        self.ButtonAdd.place(relx=0.439, rely=0.883, height=41, width=101)
        self.ButtonAdd.configure(command=lambda:add_support.register(self.EntryRU.get(),self.EntryName.get(),self.EntryAge.get(),self.EntrySex.get()))
        self.ButtonAdd.configure(text='''Register''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.264, rely=0.432, height=21, width=59)
        self.Label2.configure(text='''Name''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.278, rely=0.583, height=21, width=39)
        self.Label3.configure(text='''Age''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.278, rely=0.752, height=21, width=69)
        self.Label4.configure(text='''Sex(M/F)''')

if __name__ == '__main__':
    vp_start_gui()




