from schInfoGUIFunction import *
from schoolByCondition import *
import tkMessageBox

"""appendArr uses the function schoolstuff from schoolByCondition to populate the array for populating the listbox.
If you want to change the filter condition, please change it in schoolByCondition.py"""

overallList = schoolstuff("","type_code")

def appendArr(x, y, z):
    del y[:]
    sch_name_arr = schoolstuff(x,z)

    for name in sch_name_arr:
        # print name
        y.append(name)

    return y

def appendConditionArr(arr,type,level,gender,returnarr):
    if len(returnarr) != 0 :
        del returnarr[:]

    resultArr = []

    if type:
        for x in arr:
            if level:
                if gender:
                    if type.lower() in x[1][0]["type_code"].lower() and level.lower() in x[1][0]["mainlevel_code"].lower() and gender.lower() in x[1][0]["nature_code"].lower():
                        resultArr.append(x)

                else:
                    if type.lower() in x[1][0]["type_code"].lower() and level.lower() in x[1][0]["mainlevel_code"].lower():
                        resultArr.append(x)

            else:
                if type in x[1][0]["type_code"]:
                    resultArr.append(x)


    elif level:
        for x in arr:
            if type:
                if gender:
                    if type.lower() in x[1][0]["type_code"].lower() and level.lower() in x[1][0]["mainlevel_code"].lower() and gender.lower() in x[1][0]["nature_code"].lower():
                        resultArr.append(x)

                else:
                    if type.lower() in x[1][0]["type_code"].lower() and level.lower() in x[1][0]["mainlevel_code"].lower():
                        resultArr.append(x)

            else:
                if level in x[1][0]["mainlevel_code"]:
                    resultArr.append(x)


    elif gender:
        for x in arr:
            if type:
                if level:
                    if type.lower() in x[1][0]["type_code"].lower() and level.lower() in x[1][0]["mainlevel_code"].lower() and gender.lower() in x[1][0]["nature_code"].lower():
                        resultArr.append(x)

                else:
                    if gender.lower() in x[1][0]["nature_code"].lower() and type.lower() in x[1][0]["type_code"].lower():
                        resultArr.append(x)

            else:
                if gender in x[1][0]["nature_code"]:
                    resultArr.append(x)

    returnarr.extend(resultArr)
    return returnarr


def schListBox(arr,x,y,z,returnarr):
    """schListBox populates the listbox based on the search substring. x is the search substring and y is the name of
    the array to be processed"""

    funcArr = appendConditionArr(arr,x,y,z,returnarr)
    if not x and not y and not z:
        Lb1.delete(0, END)
    else:
        Lb1.delete(0, END)

        for schName in funcArr:
            Lb1.insert(END, schName[0])
    if len(returnarr) == 0:
        """Messagebox pops up when there is no such school"""
        tkMessageBox.showinfo("", "There is no such school")



    # for z in y:
    #     print z


def printtest(x):
    print x

top = Tk()



top.geometry("1000x500")


typeCodeArray = [""]
natureCodeArray = [""]
sessionCodeArray = [""]
schoolLevelArray = [""]
areaarray = [""]

schArray = []
"""You can change the column you want you populate in the dropdown box below here"""
for x in schoolstuff("","type_code"):
        if x[1][0]["type_code"] not in typeCodeArray:
            typeCodeArray.append(x[1][0]["type_code"])

for x in schoolstuff("","nature_code"):
        if x[1][0]["nature_code"] not in natureCodeArray:
            natureCodeArray.append(x[1][0]["nature_code"])

for x in schoolstuff("", "mainlevel_code"):
    if x[1][0]["mainlevel_code"] not in schoolLevelArray:
        schoolLevelArray.append(x[1][0]["mainlevel_code"])

filterFrame = Frame(top)
filterFrame.pack(side=TOP)
filterFrame.place(y=5,height=300, width=200,relx=0.1)


# School Level Type Dropdown
schoollevelframe = Frame(filterFrame)
schoollevelframe.pack()
L2 = Label(schoollevelframe, text="Student Level")
L2.pack()
variable2 = StringVar(schoollevelframe)
variable2.set("") # default value

"""You can change the column you want you filter below here"""
y = OptionMenu(schoollevelframe,variable2,*schoolLevelArray)
y.bind('<<OptionMenuSelect>>', lambda event: appendConditionArr(overallList,variable.get(),variable2.get(),variable1.get(),schArray))
y.pack()


# School Type Dropdown
typecodeframe = Frame(filterFrame)
typecodeframe.pack()
L1 = Label(typecodeframe, text="School Type")
L1.pack()
variable = StringVar(typecodeframe)
variable.set("") # default value

"""You can change the column you want you filter below here"""
w = OptionMenu(typecodeframe,variable,*typeCodeArray)
w.bind('<<OptionMenuSelect>>', lambda event: appendConditionArr(overallList,variable.get(),variable2.get(),variable1.get(),schArray))
w.pack()



# Student Gender Type Dropdown
naturecodeframe = Frame(filterFrame)
naturecodeframe.pack()
L2 = Label(naturecodeframe, text="Student Gender Type")
L2.pack()
variable1 = StringVar(naturecodeframe)
variable1.set("") # default value

"""You can change the column you want you filter below here"""
x = OptionMenu(naturecodeframe,variable1,*natureCodeArray)
x.bind('<<OptionMenuSelect>>', lambda event: appendConditionArr(overallList,variable.get(),variable2.get(),variable1.get(),schArray))
x.pack()



"""Change the filter by changing the column name of the last argument of schListBox"""
B = Button(top, text="Search", command=lambda: schListBox(overallList,variable.get(),variable2.get(),variable1.get(),schArray))

B.pack()

frame = Frame(top)
frame.place(y=230,height=300, relwidth=0.3,relx=0.5,anchor="center")
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

Lb1 = Listbox(frame, height=30, width=100)

"""Lb1.bind contains the onclick event of the listBox. Lb1.curselection() is just the position number of each member 
in the listbox i.e first member will be position number 0 and so on"""
Lb1.bind('<<ListboxSelect>>', lambda event:printInfo(schArray[Lb1.curselection()[0]][0],Toplevel()))  # Toplevel() just lets the function to be opened in a new window

Lb1.pack(fill=X,expand=1)

Lb1.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=Lb1.yview)

top.mainloop()
