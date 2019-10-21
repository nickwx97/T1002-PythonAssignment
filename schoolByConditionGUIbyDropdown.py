from schInfoGUIFunction import *
from schoolByCondition import *

"""appendArr uses the function schoolstuff from schoolByCondition to populate the array for populating the listbox.
If you want to change the filter condition, please change it in schoolByCondition.py"""


def appendArr(x1, y, z):
    del y[:]
    sch_name_arr = schoolstuff(x1, z)

    for name in sch_name_arr:
        y.append(name)

    return y


def schListBox(x1, y, z):
    """schListBox populates the listbox based on the search substring. x1 is the search substring and y is the name of
    the array to be processed"""

    if x1 == "":
        del y[:]
        Lb1.delete(0, END)
    else:
        del y[:]
        Lb1.delete(0, END)
        appendArr(x1, y, z)
        for schName in y:
            Lb1.insert(END, schName[0])


top = Tk()

top.geometry("1000x500")

L1 = Label(top, text="School Area")
L1.pack()

schArray = []

areaarray = []

"""You can change the column you want you populate in the dropdown box below here"""
for x in schoolstuff("", "dgp_code"):
    if x[1][0]["dgp_code"] not in areaarray:
        areaarray.append(x[1][0]["dgp_code"])

variable = StringVar(top)
variable.set("")

"""You can change the column you want you filter below here"""
w = OptionMenu(top, variable, *areaarray, command=lambda func: schListBox(variable.get(), schArray, 'dgp_code'))
w.pack()

frame = Frame(top)
frame.place(y=230, height=300, relwidth=0.3, relx=0.5, anchor="center")
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

Lb1 = Listbox(frame, height=30, width=100)
"""Lb1.bind contains the onclick event of the listBox. Lb1.curselection() is just the position number of each member 
in the listbox i.e first member will be position number 0 and so on"""
Lb1.bind('<<ListboxSelect>>', lambda event: printInfo(schArray[Lb1.curselection()[0]][0],
                                                      Toplevel()))

Lb1.pack(fill=X, expand=YES)

Lb1.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=Lb1.yview)

"""Change the filter by changing the column name of the last argument of schListBox"""

top.mainloop()
