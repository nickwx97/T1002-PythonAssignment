import csv
import schoolInfo
# !/usr/bin/python


import tkMessageBox
from Tkinter import *

def callTk():
    top = Tk()

    return top

def messageBox(x):
    top = callTk()
    frame = Frame(top)
    frame.place(rely=0.1, relheight=0.6, relwidth=1.0)
    var = StringVar()
    label = Message(frame, textvariable=var, bd=6, relief=SUNKEN)

    top.geometry("1000x500")
    top.title("School Guide")

    var.set(x)
    label.pack(side=TOP)
    label.place(y=80, relwidth=1, height=200)
    top.mainloop()

def printInfo(x):
    try:
        if x == "":
            messageBox("")
        else:
            schstuff = schoolInfo.schoolstuff(x)
            messageBox(schstuff)

    except:
        messageBox("No such school found!")





