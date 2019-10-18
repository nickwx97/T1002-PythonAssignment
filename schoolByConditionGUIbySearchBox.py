from schInfoGUIFunction import *
from schoolByCondition import *

"""appendArr uses the function schoolstuff from schoolByCondition to populate the array for populating the listbox.
If you want to change the filter condition, please change it in schoolByCondition.py"""


def appendArr(x, y, z):
    del y[:]
    sch_name_arr = schoolstuff(x, z)

    for name in sch_name_arr:
        # print name
        y.append(name)

    return y


def schListBox(x, y, z):
    """schListBox populates the listbox based on the search substring. x is the search substring and y is the name of
    the array to be processed"""

    if x == "":
        del y[:]
        Lb1.delete(0, END)
    else:
        del y[:]
        Lb1.delete(0, END)
        appendArr(x, y, z)
        for schName in y:
            Lb1.insert(END, schName[0])

    # for z in y:
    #     print z


top = Tk()

top.geometry("1000x500")

"""Change the label of the search box in the text option below"""
L1 = Label(top, text="School Area")
L1.pack()
E1 = Entry(top, bd=5)
E1.pack()
"""Change the filter by changing the column name of the last argument of schListBox"""
B = Button(top, text="Hello", command=lambda: schListBox(E1.get(), schArray, 'dgp_code'))

B.pack()

schArray = []

frame = Frame(top)
frame.place(rely=0.5, relheight=0.6, relwidth=1.0)

Lb1 = Listbox(top, height=20, width=50)
# appendArr('bedok',schArray,'dgp_code')
"""Lb1.bind contains the onclick event of the listBox. Lb1.curselection() is just the position number of each member 
in the listbox i.e first member will be position number 0 and so on"""
Lb1.bind('<<ListboxSelect>>', lambda event: printInfo(schArray[Lb1.curselection()[0]][0],
                                                      Toplevel()))  # Toplevel() just lets the function to be opened in a new window
Lb1.pack()

top.mainloop()
