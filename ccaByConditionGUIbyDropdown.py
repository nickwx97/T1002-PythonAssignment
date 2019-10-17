from cca import *
from schInfoGUIFunction import *
"""appendArr uses the function schoolstuff from schoolByCondition to populate the array for populating the listbox.
If you want to change the filter condition, please change it in schoolByCondition.py"""


def appendArr(y, z):
    print y
    del y[:]
    print y
    sch_name_arr = schoolstuff("",z)

    for name in sch_name_arr:
        # print name
        y.append(name)

    return y
#
#
#
# def schListBox(x,y,z):
#     """schListBox populates the listbox based on the search substring. x is the search substring and y is the name of
#     the array to be processed"""
#     schlistarr = []
#
#     if x=="":
#         del y[:]
#         Lb1.delete(0, END)
#     else:
#         del y[:]
#         Lb1.delete(0, END)
#         appendArr(y, z)
#
#         for schName in y:
#             for ccaName in cca.listCcaFromSch(schName[0]):
#                 if x.upper() in ccaName.upper():
#                     schlistarr.append(schName)
#         del y[:]
#         for names in schlistarr:
#             y.append([names[0]])
#             Lb1.insert(END, names[0])
#
#     # for z in y:
#     #     print z

def appendCCAs():
    arr = cca.listCcaFromSch("")
    ccaarray = []
    for i in arr:
        if i not in ccaarray:
            ccaarray.append(i)

    return sorted(ccaarray)

def listBox(selected, arr):
    itemsarr = []
    if selected == "":
        del arr[:]
        Lb1.delete(0,END)
    else:
        del arr[:]
        Lb1.delete(0, END)
        appendArr(selected, arr)

    c = cca.searchDict(value=selected)
    for items in sorted(c):
        Lb1.insert(END, items[0])

top = Tk()
top.geometry("1000x500")

L1 = Label(top, text="CCAs")
L1.pack()


ccaArray = []
variable = StringVar(top)
variable.set("") # default value

"""You can change the column you want you filter below here"""
w = OptionMenu(top,variable,*appendCCAs(),command=lambda func: listBox(variable.get(), ccaArray))
w.pack()


frame = Frame(top)
frame.place(y=230,height=300, relwidth=0.3,relx=0.5,anchor="center")
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

Lb1 = Listbox(frame, height=30, width=100)

# appendArr('bedok',schArray,'dgp_code')
"""Lb1.bind contains the onclick event of the listBox. Lb1.curselection() is just the position number of each member 
in the listbox i.e first member will be position number 0 and so on"""
arr = appendArr(ccaArray, 'dgp_code')
Lb1.bind('<<ListboxSelect>>', lambda event: printInfo(arr[Lb1.curselection()[0]][0],Toplevel()))  # Toplevel() just lets the function to be opened in a new window

Lb1.pack(fill=X,expand=YES)

Lb1.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=Lb1.yview)

"""Change the filter by changing the column name of the last argument of schListBox"""
# B = Button(top, text="Search", command=lambda: schListBox(variable.get(),schArray,'dgp_code'))

# B.pack()
top.mainloop()
