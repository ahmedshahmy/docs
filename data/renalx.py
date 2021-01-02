

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


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    init(w, top, *args, **kwargs)
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
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("623x450+542+205")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.title("CKD Progression Analyzer .beta. maa.shahmy@gmail.com ")

        self.Entryname = tk.Entry(top)
        self.Entryname.place(relx=0.316, rely=0.2, height=33, relwidth=0.266)
        self.Entryname.configure(background="white")
        self.Entryname.configure(font="TkFixedFont")

        self.Labeldate = tk.Label(top)
        self.Labeldate.place(relx=0.05, rely=0.4, height=21, width=134)
        self.Labeldate.configure(text='''Date(MM/DD/YYYY)''')

        self.Labelname = tk.Label(top)
        self.Labelname.place(relx=0.183, rely=0.2, height=21, width=41)
        self.Labelname.configure(text='''RU''')

        self.Entrydate = tk.Entry(top)
        self.Entrydate.place(relx=0.316, rely=0.4, height=33, relwidth=0.266)
        self.Entrydate.configure(background="white")
        self.Entrydate.configure(font="TkFixedFont")

        self.Labelcreat = tk.Label(top)
        self.Labelcreat.place(relx=0.133, rely=0.5, height=21, width=82)
        self.Labelcreat.configure(text='''Creatinine''')

        self.Entrycreat = tk.Entry(top)
        self.Entrycreat.place(relx=0.316, rely=0.5,
                              height=33, relwidth=0.266)
        self.Entrycreat.configure(background="white")
        self.Entrycreat.configure(font="TkFixedFont")

        self.Labelhb = tk.Label(top)
        self.Labelhb.place(relx=0.133, rely=0.6, height=21, width=82)
        self.Labelhb.configure(text='''Hemoglobin''')

        self.Entryhb = tk.Entry(top)
        self.Entryhb.place(relx=0.316, rely=0.6,
                              height=33, relwidth=0.266)
        self.Entryhb.configure(background="white")
        self.Entryhb.configure(font="TkFixedFont")

        self.Buttonadd = tk.Button(top)
        self.Buttonadd.place(relx=0.1, rely=0.867, height=31, width=131)
        self.Buttonadd.configure(command=lambda: add(
            self.Entryname.get(), self.Entrydate.get(), self.Entrycreat.get(), self.Entryhb.get()))
        self.Buttonadd.configure(text='''Add to Database''')

        self.menubar = tk.Menu(top, font="TkMenuFont",
                               bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.Buttongraph = tk.Button(top)
        self.Buttongraph.place(relx=0.483, rely=0.767, height=31, width=121)
        self.Buttongraph.configure(command=lambda: graph(self.Entryname.get()))
        self.Buttongraph.configure(text='''Cr Progression''')

        self.Buttongraph1 = tk.Button(top)
        self.Buttongraph1.place(relx=0.483, rely=0.867, height=31, width=121)
        self.Buttongraph1.configure(command=lambda: graph1(self.Entryname.get()))
        self.Buttongraph1.configure(text='''Hb Progression''')


firebasConfig = {
    'apiKey': "AIzaSyAyOKsYNnwrxwgmMy-7qQsT7QiYIcWF3-I",
    'authDomain': "renal-1e0ac.firebaseapp.com",
    'databaseURL': "https://renal-1e0ac.firebaseio.com",
    'projectId': "renal-1e0ac",
    'storageBucket': "renal-1e0ac.appspot.com",
    'messagingSenderId': "39709818947",
    'appId': "1:39709818947:web:8998d016a6d9e4ffa854f6",
    'measurementId': "G-1R80GQM1G8"
}

firebase = pyrebase.initialize_app(firebasConfig)
db = firebase.database()
auth = firebase.auth()

#global x
#global y
global user
global passwd
user = ""
passwd = ""

#global x1
#global y1
#x1 = []
#y1 = []
#global unitnum


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def add(name, date, creat, hb):
    #user = auth.refresh(user['refreshToken'])
    
    date1 = date+"  "
    data = {"RU": name, "date": date1, "Creatinine": creat}
    db.child("Creat").push(data, user['idToken'])
    print('Cr data added..')

    data1 = {"RU": name, "date": date, "Hb": hb}
    db.child("Hb").push(data1, user['idToken'])
    print('Hb data added..')
    sys.stdout.flush()


def graph1(name):
    x = []
    y = []

    #user = auth.refresh(user['refreshToken'])

    patients = db.child("Hb").order_by_child(
        "RU").equal_to(name).get(user['idToken'])

    patientdata = db.child("patientdata").order_by_child(
        "RU").equal_to(name).get(user['idToken'])
    
    ptname=""

    for pp in patientdata.each():
        
        try:
            ptname=pp.val()["Name"]
            
        except Exception as e:
            print(e)
    

    
    for p in patients.each():

        # print(p.val()["date"])
        try:

            y.append(float(p.val()["Hb"]))
            x.append(datetime.strptime(p.val()["date"], '%m/%d/%Y'))
        except Exception as e:
            print(e)
            continue

    #print(x,y)

    try:
        plt.scatter(x, y)
    except Exception as e:
        print(e)
        
    # plt.plot(x,y)
    #print(x, y)
    plt.yticks(y)

    # plt.plot(x,y)
    
    plt.title(ptname)


    
    plt.xticks(x)
    plt.yticks(y)

    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
    ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())

    plt.axhline(y=10, color='green', label='Hb=10')
    plt.axhline(y=8, color='red', label='Hb=8')

    plt.xlabel("date")
    plt.ylabel("Hb")
    plt.xticks(rotation=70)
    mng = plt.get_current_fig_manager()
    mng.resize(800, 800)
    plt.legend()
    plt.show()

    print('graph loading..')

    sys.stdout.flush()
    # plt.yticks([100,200,300,400,500,600,700,800,900,1000])


def graph(name):
    # print(auth.current_user)
    # auth.sign_in_with_email_and_password(usr,passwd)
    x = []
    y = []

    #user = auth.refresh(user['refreshToken'])

    patients = db.child("Creat").order_by_child(
        "RU").equal_to(name).get(user['idToken'])
    patientdata = db.child("patientdata").order_by_child(
        "RU").equal_to(name).get(user['idToken'])
    #print(patientdata)

    gfr20 = 0
    gfr15 = 0
    gfr10 = 0

    ptname=""

    for pp in patientdata.each():
        #print(pp)
        sexval = 0
        ageval = 0
        try:
            ptname=pp.val()["Name"]
            age = float(pp.val()["Age"])
            ageval = pow(age, -0.203)

            sex = pp.val()["Sex"]
            if sex == "M":
                sexval = 1.0
            if sex == "F":
                sexval = 0.742
        except Exception as e:
            print(e)
        #print(ageval)
        #print(sexval)

        try:
            gfr20 = float(((20/(175*ageval*sexval)) **
                           (1/float(-1.154)))/0.0113)
            gfr15 = float(((15/(175*ageval*sexval)) **
                           (1/float(-1.154)))/0.0113)
            gfr10 = float(((10/(175*ageval*sexval)) **
                           (1/float(-1.154)))/0.0113)
            gfr05 = float(((5/(175*ageval*sexval)) **
                           (1/float(-1.154)))/0.0113)

        except Exception as e:
            print(e)

        #print(gfr20)
        #print(gfr15)
        #print(gfr10)
        #print(gfr05)

    for p in patients.each():

        # print(p.val()["date"])
        try:

            y.append(float(p.val()["Creatinine"]))
            x.append(datetime.strptime(p.val()["date"], '%m/%d/%Y'))
        except Exception as e:
            print(e)
            continue

    plt.scatter(x, y)
    # plt.plot(x,y)
    #print(x, y)
    plt.yticks(y)

    # plt.plot(x,y)
    plt.axhline(y=gfr20, color='green', label='eGFR=20')
    plt.axhline(y=gfr15, color='blue', label='eGFR=15')
    plt.axhline(y=gfr10, color='orange', label='eGFR=10')
    plt.axhline(y=gfr10, color='red', label='eGFR=5')
    plt.yscale('log')
    plt.gca().invert_yaxis()
    plt.xticks(x)
    plt.yticks(y)


    plt.title(ptname)

    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
    ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())

    plt.xlabel("date")
    plt.ylabel("-log. S.Cr")
    plt.xticks(rotation=70)
    mng = plt.get_current_fig_manager()
    mng.resize(800, 800)
    plt.legend()
    plt.show()

    print('graph loading..')

    sys.stdout.flush()
    # plt.yticks([100,200,300,400,500,600,700,800,900,1000])


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    try:

        usr = input("Enter Email:")
        passwd = input("Enter password:")
        #usr="maa.shahmy@gmail.com"
        #passwd="19880113"
        user = auth.sign_in_with_email_and_password(usr, passwd)
    except:
        print("Invalid Username or password")
        exit()

    vp_start_gui()
