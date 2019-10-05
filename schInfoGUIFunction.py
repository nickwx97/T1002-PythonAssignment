import csv
import schoolInfo
# !/usr/bin/python


import tkMessageBox
from Tkinter import *

def callTk():
    top = Tk()

    return top

def messageBox(x,y):
    frame = Frame(y)
    frame.place(rely=0.1, relheight=0.6, relwidth=1.0)
    var = StringVar()
    label = Message(frame, textvariable=var, bd=6, relief=SUNKEN)

    y.geometry("1000x500")
    y.title("School Guide")

    var.set(x)
    label.pack(side=TOP)
    label.place(y=80, relwidth=1, height=200)
    y.mainloop()

def printInfo(x,y):
    try:
        if x == "":
            messageBox("")
        else:
            schstuff = schoolInfo.schoolstuff(x)
            messageBox(schstuff,y)

    except:
        messageBox("No such school found!")





