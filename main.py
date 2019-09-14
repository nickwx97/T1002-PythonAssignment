import Tkinter
from Tkinter import *
import tkFileDialog

window = Tk()
window.title("Assignment")
window.geometry('500x500')
lbl = Label(window, text="Label1")
lbl.grid(column=0, row=0)
in_path = None


def clicked():
    in_path = tkFileDialog.askopenfilename()
    lbl.configure(text=in_path)


btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()
