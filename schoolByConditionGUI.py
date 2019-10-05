from Tkinter import *
from schoolByCondition import *
from schInfoGUIFunction import *

def appendArr(x,y):
    del y[:]
    schNameArr = schoolstuff(x)

    for name in schNameArr:
        y.append(name)

    return y

def schListBox(y,z):
    Lb1.delete(0, END)
    if not y:
        Lb1.delete(0, END)
    else:
        schNameArr = appendArr(y, z)
        for schName in schNameArr:
            Lb1.insert(END, schName[0])

def printStr(x):
    print x

schArray = []

top = Tk()

top.geometry("1000x500")

L1 = Label(top, text="School Area")
L1.pack()
E1 = Entry(top, bd =5)
E1.pack()

frame = Frame(top)
frame.place(rely=0.5, relheight=0.6, relwidth=1.0)

Lb1 = Listbox(top,height=20,width=50)
Lb1.bind('<<ListboxSelect>>', lambda event: printInfo(schArray[Lb1.curselection()[0]][0],Toplevel()))
Lb1.pack()


schListBox("","")


B = Button(top, text ="Hello", command = lambda: schListBox(E1.get(),schArray))

B.pack()
top.mainloop()