from tkinter import *
import matplotlib.pyplot as plt

def click():
    x=1

window=Tk()
window.title("Test")
#window.configure(background="black")
Label(window, text="date:").grid(row=0,column=0)
dateentry=Entry(window)
dateentry.grid(row=0,column=1)

Button(window, text="click", command=click).grid(row=0, column=5)

#x=[2,3,4,5]
#y=[3,2,1,0]



window.mainloop()
#plt.plot(x,y)
#plt.show()

