from Tkinter import *
import tkMessageBox
import Tkinter as tk

from schoolInfo import *

"""Import for output display"""
from schInfoGUIFunction import *
from schoolByCondition import *
from cutoff import *
from subjectsOffered import *


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.grid()

        self.frames = {}
        for F in (StartPage, SearchPage, SubjectPage, CutOffPage, LocationPage):
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
        button1 = tk.Button(self, text="Search By Name", width=20, command=lambda: controller.show_frame("SearchPage"))
        button2 = tk.Button(self, text="Search By Subject", width=20,
                            command=lambda: controller.show_frame("SubjectPage"))
        button3 = tk.Button(self, text="Search By Cut Off Points", width=20,
                            command=lambda: controller.show_frame("CutOffPage"))
        button4 = tk.Button(self, text="Search By Location", width=20,
                            command=lambda: controller.show_frame("LocationPage"))
        self.quit = tk.Button(self, text="quit", width=20, command=self.quit)
        button1.grid(row=1, column=2)
        button2.grid(row=2, column=2)
        button3.grid(row=3, column=2)
        button4.grid(row=4, column=2)
        self.quit.grid(row=5, column=2)
        self.grid_columnconfigure((0, 4), weight=1)


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
        self.B1 = tk.Button(self, text="Search", command=lambda: schListBox(self.E1.get(),schArray,'dgp_code'))
        self.B1.grid(row=3, column=1)
        Lb1 = Listbox(self, height=10, width=50)
        Lb1.bind('<<ListboxSelect>>', lambda event: printInfo(listBoxArray[Lb1.curselection()[0]][0],
                                                              Toplevel()))  # Toplevel() just lets the function to be opened in a new window
        Lb1.grid(row=4, column=1)

        scrollbar = Scrollbar(self)
        scrollbar.grid(row=4, column=2, sticky=N + S + W)
        Lb1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=Lb1.yview)
        #labeself.L1 = tk.Frame(self, borderwidth=5, relief="sunken", width=300, height=200)
        #labeself.L1.grid(column=1, row=4, columnspan=3, rowspan=2, sticky=(N, S, E, W))
        self.back = tk.Button(self, text="self.back", width=20, command=lambda: controller.show_frame("StartPage"))
        self.quit = tk.Button(self, text="self.quit", width=20, command=self.quit)
        self.back.grid(row=6, column=1)
        self.quit.grid(row=7, column=1)
        self.grid_columnconfigure((1, 7), weight=1)


class SubjectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def messageBox(x):
            """messageBox generates the box which contains a string. x is the string to be printed, y is the tkinter
            widget location. It is usually Tk(). DO NOT USE THIS FUNCTION TO CALL OUT THE BOX. FOR LOCAL USE ONLY"""
            #label = Message(self, textself.variable=var, bd=6, relief=SUNKEN)
            label1 = Message(self, textvar=var, bd=6, relief=SUNKEN)
            label1.grid(column=1, row=4, columnspan=3, rowspan=2, sticky=(N, S, E, W))
            #label.grid(column=1, row=4)
            var.set(x)

        def printInfo(x):
            """printInfo generates the messageBox outside of the function. x is the search string and y is the tkinter
            widget location. It is usually Tk(). Use this function to call out the messagebox"""
            try:

                    so = SubjectsOffered()
                    so.createDict()
                    schoolstuff = so.getSubjectsByLevel(x)
                    for i in schoolstuff:
                        num=0
                        l = Checkbutton(self, text=str(i), var=num)
                        l.grid()
                        num+1


            except:  # DO NOT USE BARE EXCEPT
                print


        var2 = tk.IntVar()
        var3 = tk.IntVar()
        var = StringVar()
        self.B1 = tk.Button(self, text="Search", command=lambda: printInfo('secondary'))
        self.B1.grid(row=1, column=2)

        #labeself.L1 = tk.Frame(self, borderwidth=5, relief="sunken", width=300, height=200)
        #labeself.L1.grid(column=1, row=4, columnspan=3, sticky=(N, S, E, W))
        # self.E1 = Entry(self, bd=5)
        # self.E1.pack(side="top")
        self.back = tk.Button(self, text="self.back", width=20, command=lambda: controller.show_frame("StartPage"))
        self.quit = tk.Button(self, text="self.quit", width=20, command=self.quit)
        self.back.grid(row=5, column=2)
        self.quit.grid(row=6, column=2)

        self.grid_columnconfigure((0, 7), weight=1)


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
        w = OptionMenu(self, self.variable, *areaarray, command=lambda func: schListBox(self.variable.get(), schArray, 'dgp_code'))
        w.grid(row=1, column=2)

        LB1 = Listbox(self, height=30, width=50)
        LB1.bind('<<ListboxSelect>>', lambda event: printInfo(schArray[LB1.curselection()[0]][0], Toplevel()))  # Toplevel() just lets the function to be opened in a new window
        LB1.grid(row=2, column=2)

        scrollbar = Scrollbar(self)
        scrollbar.grid(row=2, column=3, sticky=N + S + W)
        LB1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=LB1.yview)

        self.back = tk.Button(self, text="self.back", width=20, command=lambda: controller.show_frame("StartPage"))
        self.quit = tk.Button(self, text="self.quit", width=20, command=self.quit)
        self.back.grid(row=5, column=2)
        self.quit.grid(row=6, column=2)


class CutOffPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.sec = Cutoff("Data/cutoff.csv")
        self.jc = Cutoff("Data/jc_cutoff.csv")
        print "hi", self.sec.search(lower=150, upper=300)

        # Secondary Cut Off
        self.L1 = tk.Label(self, text="Secondary Cut Off: ")
        self.L1.grid(row=1, column=1, columnspan=3)

        self.mini = tk.Label(self, text="minimum: ")
        self.mini.grid(row=2, column=1)
        self.E1 = tk.Entry(self, bd=5)
        self.E1.grid(row=2, column=3)

        self.maxi = tk.Label(self, text="maximum: ")
        self.maxi.grid(row=3, column=1)

        self.E2 = tk.Entry(self, bd=5)
        self.E2.grid(row=3, column=3)

        self.B1 = tk.Button(self, text="Search", width=12, command=lambda: self.printInfo(self.E1.get(), self.E2.get()))
        self.B1.grid(row=4, column=3)

        # JC cut off
        self.L3 = tk.Label(self, text="JC Cut Off: ")
        self.L3.grid(row=1, column=5)

        self.variable = StringVar()
        self.variable.set(self.jc.getHeaders()[1])

        self.stream = OptionMenu(self, self.variable, self.jc.getHeaders()[1], self.jc.getHeaders()[2])
        self.stream.grid(row=2, column=5)

        self.E3 = tk.Entry(self, bd=5)
        self.E3.grid(row=3,column=5)

        self.B2 = tk.Button(self, text="Search", command=lambda: self.JCprintInfo(self.variable.get(), self.E3.get()))
        self.B2.grid(row=4, column=5)

        self.back = tk.Button(self, text="self.back", width=20, command=lambda: controller.show_frame("StartPage"))
        self.quit = tk.Button(self, text="self.quit", width=20, command=self.quit)
        self.back.grid(row=9, column=4)
        self.quit.grid(row=10, column=4)

    def JCmessageBox(self, x):
        var = StringVar()
        label = Message(self, textvar=var, bd=6, relief=SUNKEN)

        var.set(x)
        label.grid(row=6, column=5)

    def messageBox(self, x):
        var2 = StringVar()
        self.L1 = Message(self, textvar=var2, bd=6, relief=SUNKEN)

        var2.set(x)
        self.L1.grid(row=6, column=2)

    def JCprintInfo(self, x, y):
        if x == "":
            tkMessageBox.showerror("Error", "Please enter input")
        else:
            out = {}
            if y.isdigit():
                info = self.jc.search(key=x, upper=y)
                if info:
                    for row in info:
                        out[row[0]] = {x.lower(): row[1][0].get(x.lower())}
                    self.JCmessageBox(out)
                else:
                    self.JCmessageBox("No school found")

            else:
                tkMessageBox.showerror("Error", "Please enter input")

    def printInfo(self, x, y):
        if x == "":
            tkMessageBox.showerror("Error", "Please enter input")
        else:
            print x, y
            print "this", self.sec.search(upper=x)
            print self.sec.search(lower=x, upper=y)


if __name__ == "__main__":
    app = App()
    app.minsize("1000", "500")
    app.mainloop()
