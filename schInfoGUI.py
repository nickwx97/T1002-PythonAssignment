import Tkinter
from Tkinter import *

import schoolInfo


def messageBox(x):
    var = StringVar()
    label = Message(frame, textvariable=var, bd=6, relief=SUNKEN)

    var.set(x)
    label.pack(side=TOP)
    label.place(y=80, relwidth=1, height=200)


def printInfo(x):
    try:
        if x == "":
            messageBox("")
        else:
            schstuff = schoolInfo.schoolstuff(x)
            messageBox(schstuff)

    except:  # DO NOT USE BARE EXCEPT
        messageBox("No such school found!")


binSwitch = True
intSwitch = False

top = Tk()
frame = Frame(top)
frame.place(rely=0.1, relheight=0.6, relwidth=1.0)

top.geometry("1000x500")
top.title("School Guide")

L1 = Label(top, text="Name of School")
L1.pack(side=TOP)
E1 = Entry(top, bd=5)
E1.pack(side=TOP)

B = Tkinter.Button(top, text="Hello", command=lambda: printInfo(E1.get()))

B.pack()

messageBox("")

top.mainloop()
