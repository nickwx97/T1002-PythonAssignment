import Tkinter

import ExportFunction
import schoolInfo
from cca import *
from schoolByCondition import *
from subjectsOffered import SubjectsOffered


def doExport(x, y):
    ExportFunction.schexport(x)
    y.lift()


def messageBox(x, y):
    """messageBox generates the box which contains a string. x1 is the string to be printed, y is the tkinter
    widget location. It is usually Tk(). DO NOT USE THIS FUNCTION TO CALL OUT THE BOX. FOR LOCAL USE ONLY"""
    frame = Frame(y)
    frame.place(y=230, height=500, relwidth=0.8, relx=0.5, anchor="center")
    frame.grid_propagate(False)
    frame.grid(padx=10, pady=10, sticky="nsew")
    # implement stretchability
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    txt = Text(frame, wrap=WORD)
    txt.grid_rowconfigure(0, weight=2)
    txt.grid_columnconfigure(0, weight=2)
    txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
    vscrollb = Tkinter.Scrollbar(frame, command=txt.yview)
    txt['yscrollcommand'] = vscrollb.set
    vscrollb.grid(row=0, column=1, sticky='nsew')
    hscrollb = Tkinter.Scrollbar(frame, command=txt.xview, orient='horizontal')
    txt['xscrollcommand'] = hscrollb.set
    hscrollb.grid(row=1, column=0, sticky='nsew')
    e1 = Tkinter.Button(frame, text="Export", width=12, command=lambda: doExport(x, y))
    e1.grid(row=1, column=0, sticky='nsew')

    y.geometry("1000x600")
    y.title("School Guide")
    y.grid_rowconfigure(0, weight=1)
    y.grid_columnconfigure(0, weight=1)
    txt.insert(INSERT, x)
    txt["state"] = DISABLED

    txt.pack(expand=1, side="bottom")
    e1.pack(expand=1, side="bottom")
    y.mainloop()


def printInfo(x, y):
    """printInfo generates the messageBox outside of the function. x1 is the search string and y is the tkinter
    widget location. It is usually Tk(). Use this function to call out the messagebox"""
    try:
        if x == "":
            messageBox("", y)
        else:
            schstuff = schoolInfo.schoolstuff(x) + '\n'
            schstuff += "-" * 80 + '\nCCA(s) offered:\n'
            c = CCA()
            for item in c.listCustomCcaFromSch(x):
                schstuff += item + '\n'
            schstuff += "-" * 80 + '\nSubject(s) offered:\n'
            s = SubjectsOffered()
            for item in s.getSubjectsBySchoolName(x):
                schstuff += item + '\n'
            messageBox(schstuff, y)

    except NoneType:
        messageBox("No such school found!", y)
