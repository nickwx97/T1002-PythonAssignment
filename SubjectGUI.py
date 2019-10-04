import Tkinter
import tkMessageBox
import csv


app = Tkinter.Tk()
app.minsize(1200, 400)
app.title = "GUI"

s1 = Tkinter.Label(app, text="School Name")
s1.grid(row=1, column=1)

school = Tkinter.StringVar()
inputs = Tkinter.Entry(app, textvariable=school)
inputs.grid(row=1, column=2)

b1 = Tkinter.Button(app, text="Search", width=7)
b1.grid(row=1, column=3)

var1 = Tkinter.IntVar()
c = Tkinter.Checkbutton(app, text="Expand", variable=var1)
c.pack()
app.mainloop()

