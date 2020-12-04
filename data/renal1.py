#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Dec 01, 2020 11:07:26 AM +0530  platform: Linux

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

import renal1_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    renal1_support.init(root, top)
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
    renal1_support.init(w, top, *args, **kwargs)
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

        top.geometry("623x450+542+205")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.title("CKD progression ")

        self.Entryname = tk.Entry(top)
        self.Entryname.place(relx=0.316, rely=0.2, height=33, relwidth=0.266)
        self.Entryname.configure(background="white")
        self.Entryname.configure(font="TkFixedFont")

        self.Labeldate = tk.Label(top)
        self.Labeldate.place(relx=0.05, rely=0.422, height=21, width=134)
        self.Labeldate.configure(text='''Date(YYYYMMDD)''')

        self.Labelname = tk.Label(top)
        self.Labelname.place(relx=0.183, rely=0.222, height=21, width=41)
        self.Labelname.configure(text='''RU''')

        self.Entrydate = tk.Entry(top)
        self.Entrydate.place(relx=0.316, rely=0.422, height=33, relwidth=0.266)
        self.Entrydate.configure(background="white")
        self.Entrydate.configure(font="TkFixedFont")

        self.Labelcreat = tk.Label(top)
        self.Labelcreat.place(relx=0.133, rely=0.667, height=21, width=82)
        self.Labelcreat.configure(text='''Creatinine''')

        self.Entrycreat = tk.Entry(top)
        self.Entrycreat.place(relx=0.316, rely=0.644, height=33, relwidth=0.266)
        self.Entrycreat.configure(background="white")
        self.Entrycreat.configure(font="TkFixedFont")

        self.Buttonadd = tk.Button(top)
        self.Buttonadd.place(relx=0.1, rely=0.867, height=31, width=131)
        self.Buttonadd.configure(command=lambda:renal1_support.add(self.Entryname.get(),self.Entrydate.get(),self.Entrycreat.get()))
        self.Buttonadd.configure(text='''Add to Database''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Buttongraph = tk.Button(top)
        self.Buttongraph.place(relx=0.483, rely=0.867, height=31, width=121)
        self.Buttongraph.configure(command=lambda:renal1_support.graph(self.Entryname.get()))
        self.Buttongraph.configure(text='''Analyze''')

if __name__ == '__main__':
    vp_start_gui()





