import Tkinter
from Tkinter import *
from schoolByCondition import *
import schoolInfo


# !/usr/bin/python


def messageBox(x, y):
    """messageBox generates the box which contains a string. x is the string to be printed, y is the tkinter
    widget location. It is usually Tk(). DO NOT USE THIS FUNCTION TO CALL OUT THE BOX. FOR LOCAL USE ONLY"""
    frame = Frame(y)
    frame.place(y=230, height=500, relwidth=0.8,relx=0.5,anchor="center")
    var = StringVar()
    label = Message(frame, textvariable=var, bd=6, relief=SUNKEN)
    e1 = Tkinter.Button(frame, text="Export", width=12)

    y.geometry("1000x600")
    y.title("School Guide")

    var.set(x)
    label.pack(expand=1, side="top")
    e1.pack(expand=1, side="bottom")
    y.mainloop()


def printInfo(x, y):
    """printInfo generates the messageBox outside of the function. x is the search string and y is the tkinter
    widget location. It is usually Tk(). Use this function to call out the messagebox"""
    try:
        if x == "":
            messageBox("",y)
        else:
            schstuff = schoolInfo.schoolstuff(x)
            messageBox(schstuff, y)

    except:  #DO NOT USE BARE EXCEPT
        messageBox("No such school found!",y)
