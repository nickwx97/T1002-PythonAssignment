from schInfoGUIFunction import *
from schoolByCondition import *

"""appendArr uses the function schoolstuff from schoolByCondition to populate the array for populating the listbox.
If you want to change the filter condition, please change it in schoolByCondition.py"""


def appendArr(x, y, z):
    del y[:]
    sch_name_arr = schoolstuff(x,z)

    for name in sch_name_arr:
        # print name
        y.append(name)

    return y



def schListBox(x,y,z):
    """schListBox populates the listbox based on the search substring. x is the search substring and y is the name of
    the array to be processed"""

    if x=="":
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




schArray = []

typeCodeArray = [""]
natureCodeArray = [""]
sessionCodeArray = [""]
schoolLevelArray = [""]
areaarray = [""]


"""You can change the column you want you populate in the dropdown box below here"""
for x in schoolstuff("","type_code"):
        if x[1][0]["type_code"] not in typeCodeArray:
            typeCodeArray.append(x[1][0]["type_code"])

for x in schoolstuff("","nature_code"):
        if x[1][0]["nature_code"] not in natureCodeArray:
            natureCodeArray.append(x[1][0]["nature_code"])

filterFrame = Frame(top)
filterFrame.pack(side=TOP)
filterFrame.place(y=5,height=300, width=200,relx=0.1)

# fffffffffffffffffffffffffffffffffffff
typecodeframe = Frame(filterFrame)
typecodeframe.pack()
L1 = Label(typecodeframe, text="School Type")
L1.pack()
variable = StringVar(typecodeframe)
variable.set("") # default value

"""You can change the column you want you filter below here"""
w = OptionMenu(typecodeframe,variable,*typeCodeArray)
w.pack()


# fffffffffffffffffffffffffffffffffffff
naturecodeframe = Frame(filterFrame)
naturecodeframe.pack()
L2 = Label(naturecodeframe, text="Student Gender Type")
L2.pack()
variable1 = StringVar(naturecodeframe)
variable1.set("") # default value

"""You can change the column you want you filter below here"""
x = OptionMenu(naturecodeframe,variable1,*natureCodeArray)
x.pack()


frame = Frame(top)
frame.place(y=230,height=300, relwidth=0.3,relx=0.5,anchor="center")
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

Lb1 = Listbox(frame, height=30, width=100)
# appendArr('bedok',schArray,'dgp_code')
"""Lb1.bind contains the onclick event of the listBox. Lb1.curselection() is just the position number of each member 
in the listbox i.e first member will be position number 0 and so on"""
Lb1.bind('<<ListboxSelect>>', lambda event: printInfo(schArray[Lb1.curselection()[0]][0],Toplevel()))  # Toplevel() just lets the function to be opened in a new window

Lb1.pack(fill=X,expand=YES)

Lb1.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=Lb1.yview)

"""Change the filter by changing the column name of the last argument of schListBox"""
# B = Button(top, text="Search", command=lambda: schListBox(variable.get(),schArray,'dgp_code'))

# B.pack()
top.mainloop()
