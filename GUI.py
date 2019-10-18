import Tkinter as tk
import tkMessageBox

from schoolInfo import *

"""Import for output display"""
from cca import *
from cutoff import *
from schInfoGUIFunction import *
from subjectsOffered import *


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.grid()

        self.frames = {}
        for F in (StartPage, OverallSearchPage, SearchPage, SubjectPage, CutOffPage, CCAPage, LocationPage):
            pagename = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[pagename] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, pagename):
        frame = self.frames[pagename]
        top = Frame(self)
        bottom = Frame(self)
        top.grid()
        bottom.grid()
        frame.tkraise()

    def quit(self):
        self.root.destroy()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="School Portal", font=("Courier", 44))
        label.grid(row=0, column=2)
        tk.title = "School Portal"
        button1 = tk.Button(self, text="General Search", width=20,
                            command=lambda: controller.show_frame("OverallSearchPage"))
        button2 = tk.Button(self, text="Search By Name", width=20, command=lambda: controller.show_frame("SearchPage"))
        button3 = tk.Button(self, text="Search By Subject", width=20,
                            command=lambda: controller.show_frame("SubjectPage"))
        button4 = tk.Button(self, text="Search By CCA", width=20,
                            command=lambda: controller.show_frame("CCAPage"))
        button5 = tk.Button(self, text="Search By Location", width=20,
                            command=lambda: controller.show_frame("LocationPage"))
        button6 = tk.Button(self, text="Search By Cut Off Points", width=20,
                            command=lambda: controller.show_frame("CutOffPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        button1.grid(row=1, column=2)
        button2.grid(row=2, column=2)
        button3.grid(row=3, column=2)
        button4.grid(row=4, column=2)
        button5.grid(row=5, column=2)
        button6.grid(row=6, column=2)
        quit.grid(row=7, column=2)


class OverallSearchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        overallList = schoolstuff("", "type_code")

        def appendArr(x, y, z):
            del y[:]
            sch_name_arr = schoolstuff(x, z)

            for name in sch_name_arr:
                # print name
                y.append(name)

            return y

        def appendConditionArr(arr, type, level, gender, returnarr):
            if len(returnarr) != 0:
                del returnarr[:]

            resultArr = []

            if type:
                for x in arr:
                    if level:
                        if gender:
                            if type.lower() in x[1][0]["type_code"].lower() and level.lower() in x[1][0][
                                "mainlevel_code"].lower() and gender.lower() in x[1][0]["nature_code"].lower():
                                resultArr.append(x)

                        else:
                            if type.lower() in x[1][0]["type_code"].lower() and level.lower() in x[1][0][
                                "mainlevel_code"].lower():
                                resultArr.append(x)

                    else:
                        if type in x[1][0]["type_code"]:
                            resultArr.append(x)

            elif level:
                for x in arr:
                    if type:
                        if gender:
                            if type.lower() in x[1][0]["type_code"].lower() and level.lower() in x[1][0][
                                "mainlevel_code"].lower() and gender.lower() in x[1][0]["nature_code"].lower():
                                resultArr.append(x)

                        else:
                            if type.lower() in x[1][0]["type_code"].lower() and level.lower() in x[1][0][
                                "mainlevel_code"].lower():
                                resultArr.append(x)

                    else:
                        if level in x[1][0]["mainlevel_code"]:
                            resultArr.append(x)

            elif gender:
                for x in arr:
                    if type:
                        if level:
                            if type.lower() in x[1][0]["type_code"].lower() and level.lower() in x[1][0][
                                "mainlevel_code"].lower() and gender.lower() in x[1][0]["nature_code"].lower():
                                resultArr.append(x)

                        else:
                            if gender.lower() in x[1][0]["nature_code"].lower() and type.lower() in x[1][0][
                                "type_code"].lower():
                                resultArr.append(x)

                    else:
                        if gender in x[1][0]["nature_code"]:
                            resultArr.append(x)

            returnarr.extend(resultArr)
            return returnarr

        def schListBox(arr, x, y, z, returnarr):
            """schListBox populates the listbox based on the search substring. x is the search substring and y is the name of
            the array to be processed"""

            funcArr = appendConditionArr(arr, x, y, z, returnarr)
            if not x and not y and not z:
                Lb1.delete(0, END)
            else:
                Lb1.delete(0, END)

                for schName in funcArr:
                    Lb1.insert(END, schName[0])
            if len(returnarr) == 0:
                """Messagebox pops up when there is no such school"""
                tkMessageBox.showinfo("", "There is no such school")

        typeCodeArray = [""]
        natureCodeArray = [""]
        sessionCodeArray = [""]
        schoolLevelArray = [""]
        areaarray = [""]

        schArray = []
        """You can change the column you want you populate in the dropdown box below here"""
        for x in schoolstuff("", "type_code"):
            if x[1][0]["type_code"] not in typeCodeArray:
                typeCodeArray.append(x[1][0]["type_code"])

        for x in schoolstuff("", "nature_code"):
            if x[1][0]["nature_code"] not in natureCodeArray:
                natureCodeArray.append(x[1][0]["nature_code"])

        for x in schoolstuff("", "mainlevel_code"):
            if x[1][0]["mainlevel_code"] not in schoolLevelArray:
                schoolLevelArray.append(x[1][0]["mainlevel_code"])

        filterFrame = Frame(self)
        filterFrame.grid()
        # filterFrame.place(y=5, height=300, width=200, relx=0.1.csv)

        # School Level Type Dropdown
        schoollevelframe = Frame(filterFrame)
        schoollevelframe.grid()
        L2 = Label(schoollevelframe, text="Student Level")
        L2.grid(column=1)
        variable2 = StringVar(schoollevelframe)
        variable2.set("")  # default value

        """You can change the column you want you filter below here"""
        y = OptionMenu(schoollevelframe, variable2, *schoolLevelArray)
        y.bind('<<OptionMenuSelect>>',
               lambda event: appendConditionArr(overallList, variable.get(), variable2.get(), variable1.get(),
                                                schArray))
        y.grid(column=1)

        # School Type Dropdown
        typecodeframe = Frame(filterFrame)
        typecodeframe.grid()
        L1 = Label(typecodeframe, text="School Type")
        L1.grid(column=1)
        variable = StringVar(typecodeframe)
        variable.set("")  # default value

        """You can change the column you want you filter below here"""
        w = OptionMenu(typecodeframe, variable, *typeCodeArray)
        w.bind('<<OptionMenuSelect>>',
               lambda event: appendConditionArr(overallList, variable.get(), variable2.get(), variable1.get(),
                                                schArray))
        w.grid(column=1)

        # Student Gender Type Dropdown
        naturecodeframe = Frame(filterFrame)
        naturecodeframe.grid()
        L2 = Label(naturecodeframe, text="Student Gender Type")
        L2.grid(column=1)
        variable1 = StringVar(naturecodeframe)
        variable1.set("")  # default value

        """You can change the column you want you filter below here"""
        x = OptionMenu(naturecodeframe, variable1, *natureCodeArray)
        x.bind('<<OptionMenuSelect>>',
               lambda event: appendConditionArr(overallList, variable.get(), variable2.get(), variable1.get(),
                                                schArray))
        x.grid(column=1)

        """Change the filter by changing the column name of the last argument of schListBox"""
        B = Button(self, text="Search", width=12,
                   command=lambda: schListBox(overallList, variable.get(), variable2.get(), variable1.get(), schArray))

        B.grid(pady=50)
        self.back = tk.Button(self, text="Back", width=12, command=lambda: controller.show_frame("StartPage"))
        self.quit = tk.Button(self, text="Quit", width=12, command=self.quit)
        self.back.grid()
        self.quit.grid()

        frame = Frame(self)
        frame.place(y=180, height=300, relwidth=0.6, relx=0.7, anchor="center")
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        Lb1 = Listbox(frame, height=30, width=200)

        """Lb1.bind contains the onclick event of the listBox. Lb1.curselection() is just the position number of each member 
        in the listbox i.e first member will be position number 0 and so on"""
        Lb1.bind('<<ListboxSelect>>', lambda event: printInfo(schArray[Lb1.curselection()[0]][0],
                                                              Toplevel()))  # Toplevel() just lets the function to be opened in a new window

        Lb1.pack(fill=X, expand=1)

        Lb1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=Lb1.yview)


class SearchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

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
                appendArr("", y, z)
                for schName in y:
                    if x.upper() in schName[0].upper():
                        Lb1.insert(END, schName[0])
                        listBoxArray.append(schName)

            # for z in y:
            #     print z

        schArray = []
        listBoxArray = []

        self.L1 = tk.Label(self, text="Name of School")
        self.L1.grid(row=1, column=1)
        self.E1 = Entry(self, bd=5)
        self.E1.grid(row=2, column=1)
        self.B1 = tk.Button(self, text="Search", width=12,
                            command=lambda: schListBox(self.E1.get(), schArray, 'dgp_code'))
        self.B1.grid(row=3, column=1)
        Lb1 = Listbox(self, height=30, width=100)
        Lb1.bind('<<ListboxSelect>>', lambda event: printInfo(listBoxArray[Lb1.curselection()[0]][0],
                                                              Toplevel()))  # Toplevel() just lets the function to be opened in a new window
        Lb1.grid(row=4, column=1)

        scrollbar = Scrollbar(self)
        scrollbar.grid(row=4, column=2, sticky=N + S + W)
        Lb1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=Lb1.yview)
        # labeself.L1 = tk.Frame(self, borderwidth=5, relief="sunken", width=300, height=200)
        # labeself.L1.grid(column=1.csv, row=4, columnspan=3, rowspan=2, sticky=(N, S, E, W))
        self.back = tk.Button(self, text="Back", width=12, command=lambda: controller.show_frame("StartPage"))
        self.quit = tk.Button(self, text="Quit", width=12, command=self.quit)
        self.back.grid(row=5, column=1)
        self.quit.grid(row=6, column=1)


class SubjectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def messageBox(x):
            """messageBox generates the box which contains a string. x is the string to be printed, y is the tkinter
            widget location. It is usually Tk(). DO NOT USE THIS FUNCTION TO CALL OUT THE BOX. FOR LOCAL USE ONLY"""
            # label = Message(self, textself.variable=var, bd=6, relief=SUNKEN)
            label1 = Message(self, textvar=var, bd=6, relief=SUNKEN)
            label1.grid(column=1, row=4, columnspan=3, rowspan=2, sticky=(N, S, E, W))
            # label.grid(column=1.csv, row=4)
            var.set(x)

        def printInfoDropdown(x):
            """printInfo generates the messageBox outside of the function. x is the search string and y is the tkinter
            widget location. It is usually Tk(). Use this function to call out the messagebox"""
            try:

                so = SubjectsOffered()
                so.createDict()
                schoolstuff = so.getSubjectsByLevel(x)
                subjectlist = []
                for i in schoolstuff:
                    subjectlist.append(i)
                subjectlist.sort()
                global subjectmenu
                global subjectmenu1
                subjectmenu1 = StringVar(self)
                subjectmenu = OptionMenu(self, subjectmenu1, *subjectlist)
                subjectmenu1.set('Select a Subject\t\t\t\t\t')  # default value
                subjectmenu.grid(row=3, column=2, sticky="ew")

                global subjectmenu2
                subjectmenu2 = StringVar(self)
                subjectmenu = OptionMenu(self, subjectmenu2, *subjectlist)
                subjectmenu2.set('Select a Subject\t\t\t\t\t')  # default value
                subjectmenu.grid(row=4, column=2, sticky="ew")

                global subjectmenu3
                subjectmenu3 = StringVar(self)
                subjectmenu = OptionMenu(self, subjectmenu3, *subjectlist)
                subjectmenu3.set('Select a Subject\t\t\t\t\t')  # default value
                subjectmenu.grid(row=5, column=2, sticky="ew")

                global subjectmenu4
                subjectmenu4 = StringVar(self)
                subjectmenu = OptionMenu(self, subjectmenu4, *subjectlist)
                subjectmenu4.set('Select a Subject\t\t\t\t\t')  # default value
                subjectmenu.grid(row=6, column=2, sticky="ew")
            except:  # DO NOT USE BARE EXCEPT
                print "error"

        tkvar = StringVar(self)

        def appendArr(x, y, z):
            del y[:]
            sch_name_arr = schoolstuff(x, z)

            for name in sch_name_arr:
                # print name
                y.append(name)

            return y

        def schListBox(drop1, drop2, drop3, drop4, y, z):
            """schListBox populates the listbox based on the search substring. x is the search substring and y is the name of
            the array to be processed"""
            schArray = []
            schFinalArray = []
            for k, v in so.filterMultiSubs([drop1, drop2, drop3, drop4]).items():
                schArray.append(k)

            del y[:]
            LB1.delete(0, END)
            appendArr("", y, z)
            for schName in y:
                for schArrayMem in schArray:
                    if schName[0].upper() in schArrayMem.upper():
                        schFinalArray.append(schName[0])
            del y[:]
            for names in schFinalArray:
                y.append(names)
                LB1.insert(END, names)

        def matchSubject(sub1, sub2, sub3, sub4):
            matchlist = []
            matchlist.append(sub1)
            matchlist.append(sub2)
            matchlist.append(sub3)
            matchlist.append(sub4)

            subjectDict = so.subjectDict()
            global schoolResult
            schoolResult = [school_name
                            for school_name, school_content in subjectDict.items()
                            if all(
                    subject in school_content
                    for subject in matchlist)]

        def reset():
            subjectmenu.grid_remove

        # Dictionary with options
        choices = {'Primary', 'Secondary', 'Junior College'}
        tkvar.set('Select Level')  # set the default option
        popupMenu = OptionMenu(self, tkvar, *choices)
        popupMenu.grid(row=0, column=2)

        schArray = []
        # link function to change dropdown
        var2 = tk.IntVar()
        var3 = tk.IntVar()
        var = StringVar()
        self.B1 = tk.Button(self, text="Apply", command=lambda: printInfoDropdown(tkvar.get()))
        self.B1.grid(row=0, column=3)
        self.B2 = tk.Button(self, text="Search",
                            command=lambda: schListBox(subjectmenu1.get(), subjectmenu2.get(), subjectmenu3.get(),
                                                       subjectmenu4.get(), schArray, 'dgp_code'))
        self.B2.grid(row=7, column=2)
        LB1 = Listbox(self, height=30, width=50)
        LB1.bind('<<ListboxSelect>>', lambda event: printInfo(schArray[LB1.curselection()[0]],
                                                              Toplevel()))  # Toplevel() just lets the function to be opened in a new window
        LB1.grid(row=8, column=2)
        self.back = tk.Button(self, text="Back", width=20, command=lambda: controller.show_frame("StartPage"))
        self.quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        self.back.grid(row=9, column=2)
        self.quit.grid(row=10, column=2)

        self.grid_columnconfigure((0, 10), weight=1)


class CCAPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.cca = CCA()

        def appendArr(y, z):
            del y[:]
            sch_name_arr = schoolstuff("", z)

            for name in sch_name_arr:
                # print name
                y.append(name)

            return y

        def schListBox(x, y, z):
            """schListBox populates the listbox based on the search substring. x is the search substring and y is the name of
            the array to be processed"""
            schlistarr = []

            if x == "":
                del y[:]
                Lb1.delete(0, END)
            else:
                del y[:]
                Lb1.delete(0, END)
                appendArr(y, z)

                for schName in y:
                    for ccaName in self.cca.listCcaFromSch(schName[0]):
                        if x.upper() in ccaName.upper():
                            schlistarr.append(schName)
                del y[:]
                for names in schlistarr:
                    y.append([names[0]])
                    Lb1.insert(END, names[0])

        L1 = Label(self, text="CCAs")
        L1.grid()

        sorted_cca = sorted(self.cca.getUniqueCcaList())

        schArray = []
        variable = StringVar(self)
        variable.set("")  # default value

        """You can change the column you want you filter below here"""
        w = OptionMenu(self, variable, *sorted_cca,
                       command=lambda func: schListBox(variable.get(), schArray, 'dgp_code'))
        w.grid()

        scrollbar = Scrollbar(self)
        scrollbar.grid(row=2, column=1, sticky=N + S + W)

        Lb1 = Listbox(self, height=30, width=100)
        """Lb1.bind contains the onclick event of the listBox. Lb1.curselection() is just the position number of each member 
        in the listbox i.e first member will be position number 0 and so on"""
        Lb1.bind('<<ListboxSelect>>', lambda event: printInfo(schArray[Lb1.curselection()[0]][0],
                                                              Toplevel()))

        Lb1.grid(row=2, column=0)

        Lb1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=Lb1.yview)
        self.back = tk.Button(self, text="Back", width=12, command=lambda: controller.show_frame("StartPage"))
        self.quit = tk.Button(self, text="Quit", width=12, command=self.quit)
        self.back.grid()
        self.quit.grid()


class LocationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        schArray = []
        areaarray = []

        for x in schoolstuff("", "dgp_code"):
            if x[1][0]["dgp_code"] not in areaarray:
                areaarray.append(x[1][0]["dgp_code"])

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
                LB1.delete(0, END)
            else:
                del y[:]
                LB1.delete(0, END)
                appendArr(x, y, z)
                for schName in y:
                    LB1.insert(END, schName[0])

        self.L1 = tk.Label(self, text="Location: ")
        self.L1.grid(row=0, column=2)

        self.variable = StringVar()
        self.variable.set("")  # default value

        """You can change the column you want you filter below here"""
        w = OptionMenu(self, self.variable, *areaarray,
                       command=lambda func: schListBox(self.variable.get(), schArray, 'dgp_code'))
        w.grid(row=1, column=2)

        LB1 = Listbox(self, height=30, width=50)
        LB1.bind('<<ListboxSelect>>', lambda event: printInfo(schArray[LB1.curselection()[0]][0],
                                                              Toplevel()))  # Toplevel() just lets the function to be opened in a new window
        LB1.grid(row=2, column=2)

        scrollbar = Scrollbar(self)
        scrollbar.grid(row=2, column=3, sticky=N + S + W)
        LB1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=LB1.yview)

        self.back = tk.Button(self, text="Back", width=12, command=lambda: controller.show_frame("StartPage"))
        self.quit = tk.Button(self, text="Quit", width=12, command=self.quit)
        self.back.grid(row=5, column=2)
        self.quit.grid(row=6, column=2)


class CutOffPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.sec = Cutoff("Data/cutoff.csv")
        self.jc = Cutoff("Data/jc_cutoff.csv")

        # Secondary Cut Off
        self.L1 = tk.Label(self, text="Secondary Cut Off: ")
        self.L1.grid(row=1, column=0, columnspan=4)

        self.mini = tk.Label(self, text="minimum: ")
        self.mini.grid(row=2, column=0)
        self.E1 = tk.Entry(self, bd=5)
        self.E1.grid(row=2, column=3)

        self.maxi = tk.Label(self, text="maximum: ")
        self.maxi.grid(row=3, column=0)

        self.E2 = tk.Entry(self, bd=5)
        self.E2.grid(row=3, column=3)

        self.B1 = tk.Button(self, text="Search", width=12,
                            command=lambda: self.SECprintInfo(self.E1.get(), self.E2.get()))
        self.B1.grid(row=4, column=3)

        # JC cut off
        self.L3 = tk.Label(self, text="JC Cut Off: ")
        self.L3.grid(row=1, column=5)

        self.variable = StringVar()
        self.variable.set(self.jc.getHeaders()[1])

        self.stream = OptionMenu(self, self.variable, self.jc.getHeaders()[1], self.jc.getHeaders()[2])
        self.stream.grid(row=2, column=5)

        self.E3 = tk.Entry(self, bd=5)
        self.E3.grid(row=3, column=5)

        self.B2 = tk.Button(self, text="Search", width=12,
                            command=lambda: self.JCprintInfo(self.variable.get(), self.E3.get()))
        self.B2.grid(row=4, column=5)

        self.back = tk.Button(self, text="Back", width=12, command=lambda: controller.show_frame("StartPage"))
        self.quit = tk.Button(self, text="Quit", width=12, command=self.quit)
        self.back.grid(row=9, column=4)
        self.quit.grid(row=10, column=4)

    def JCmessageBox(self, x):
        top = Toplevel()
        top.title("JC Cut Off Points")
        top.minsize("1000", "500")
        scrollbar = Scrollbar(top)
        scrollbar.pack(side=RIGHT, fill=Y)
        L2 = Listbox(top, height=30, width=100)
        e1 = tk.Button(top, text="Export", width=12, command=lambda: ExportFunction.JCexport([self.jc.getHeaders()[0],
                                                                                              self.variable.get()], x))
        for k, v in x.items():
            L2.insert(END, str(k) + ": " + str(v))
        L2.pack(expand=YES)
        L2.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=L2.yview)
        e1.pack(expand=1, side="bottom", pady=20)

    def JCprintInfo(self, x, y):
        if x == "":
            tkMessageBox.showerror("Error", "Please enter input")
        else:
            out = {}
            if y.isdigit():
                info = self.jc.search(key=x, upper=int(y)).sort(key=x)
                if info:
                    for row in info:
                        out[row[0]] = row[1][0].get(x.lower())
                    self.JCmessageBox(out)
                else:
                    tkMessageBox.showerror("Error", "No schools found")

            else:
                tkMessageBox.showerror("Error", "Please enter input")

    def messageBox(self, x):
        top = Toplevel()
        top.title("Secondary Cut Off Points")
        top.minsize("1000", "500")

        scrollbar = Scrollbar(top)
        scrollbar.pack(side=RIGHT, fill=Y)

        L1 = Listbox(top, height=30, width=100)
        e1 = tk.Button(top, text="Export", width=12, command=lambda: ExportFunction.export(self.sec.getHeaders(), dict(x)))
        for k, v in x:
            L1.insert(END, str(k) + ": " + str(v))
        L1.pack(expand=YES)
        L1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=L1.yview)
        e1.pack(expand=1, side="bottom", pady=20)

    def SECprintInfo(self, x, y):
        if x == "":
            tkMessageBox.showerror("Error", "Please enter input")
        else:
            out = {}
            if y.isdigit():
                secinfo = self.sec.search(lower=int(x))
                if secinfo:
                    for col, row in secinfo.items():
                        out[col] = row[0].get('cutoff')
                    out = sorted(out.items(), key=lambda kv: kv[1], reverse=True)
                    self.messageBox(out)
                else:
                    tkMessageBox.showerror("Error", "No schools found")
            else:
                tkMessageBox.showerror("Error", "No schools found")


if __name__ == "__main__":
    app = App()
    app.minsize("900", "400")
    app.title("School Portal")
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.mainloop()
