from Tkinter import *
import tkMessageBox
import Tkinter as tk
from schoolInfo import *

"""Import for output display"""
from schInfoGUIFunction import *
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
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        button1.grid(row=1, column=2)
        button2.grid(row=2, column=2)
        button3.grid(row=3, column=2)
        button4.grid(row=4, column=2)
        quit.grid(row=5, column=2)
        self.grid_columnconfigure((0, 4), weight=1)


class SearchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        def messageBox(x):
            """messageBox generates the box which contains a string. x is the string to be printed, y is the tkinter
            widget location. It is usually Tk(). DO NOT USE THIS FUNCTION TO CALL OUT THE BOX. FOR LOCAL USE ONLY"""
            #label = Message(self, textvariable=var, bd=6, relief=SUNKEN)
            label1 = Message(self, textvariable=var, bd=6, relief=SUNKEN)
            label1.grid(column=1, row=4, columnspan=3, rowspan=2, sticky=(N, S, E, W))
            #label.grid(column=1, row=4)
            var.set(x)

        def printInfo(x):
            """printInfo generates the messageBox outside of the function. x is the search string and y is the tkinter
            widget location. It is usually Tk(). Use this function to call out the messagebox"""
            try:
                if x == "":
                    messageBox("")
                else:
                    schstuff = schoolstuff(x)
                    messageBox(schstuff)

            except:  # DO NOT USE BARE EXCEPT
                messageBox("No such school found!")
        var = StringVar()

        L1 = tk.Label(self, text="Name of School")
        L1.grid(row=1, column=1)
        E1 = Entry(self, bd=5)
        E1.grid(row=2, column=1)
        B1 = tk.Button(self, text="Search", command=lambda: printInfo(E1.get()))
        B1.grid(row=3, column=1)
        messageBox("")
        #label1 = tk.Frame(self, borderwidth=5, relief="sunken", width=300, height=200)
        #label1.grid(column=1, row=4, columnspan=3, rowspan=2, sticky=(N, S, E, W))
        back = tk.Button(self, text="Back", width=20, command=lambda: controller.show_frame("StartPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        back.grid(row=6, column=1)
        quit.grid(row=7, column=1)
        self.grid_columnconfigure((1, 7), weight=1)


class SubjectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def messageBox(x):
            """messageBox generates the box which contains a string. x is the string to be printed, y is the tkinter
            widget location. It is usually Tk(). DO NOT USE THIS FUNCTION TO CALL OUT THE BOX. FOR LOCAL USE ONLY"""
            #label = Message(self, textvariable=var, bd=6, relief=SUNKEN)
            label1 = Message(self, textvariable=var, bd=6, relief=SUNKEN)
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
                        l = Checkbutton(self, text=str(i), variable=num)
                        l.grid()
                        num+1


            except:  # DO NOT USE BARE EXCEPT
                print


        var2 = tk.IntVar()
        var3 = tk.IntVar()
        var = StringVar()
        B1 = tk.Button(self, text="Search", command=lambda: printInfo('secondary'))
        B1.grid(row=1, column=2)
        #label1 = tk.Frame(self, borderwidth=5, relief="sunken", width=300, height=200)
        #label1.grid(column=1, row=4, columnspan=3, sticky=(N, S, E, W))
        # E1 = Entry(self, bd=5)
        # E1.pack(side="top")
        back = tk.Button(self, text="Back", width=20, command=lambda: controller.show_frame("StartPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        back.grid(row=5, column=2)
        quit.grid(row=6, column=2)

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
                Lb1.delete(0, END)
            else:
                del y[:]
                Lb1.delete(0, END)
                appendArr(x, y, z)
                for schName in y:
                    Lb1.insert(END, schName[0])

        L1 = tk.Label(self, text="Location: ")
        L1.grid(row=0, column=2)

        variable = StringVar()
        variable.set("")  # default value

        """You can change the column you want you filter below here"""
        w = OptionMenu(self, variable, *areaarray, command=lambda func: schListBox(variable.get(), schArray, 'dgp_code'))
        w.grid(row=1, column=2)

        Lb1 = Listbox(self, height=30, width=50)
        Lb1.bind('<<ListboxSelect>>', lambda event: printInfo(schArray[Lb1.curselection()[0]][0], Toplevel()))  # Toplevel() just lets the function to be opened in a new window
        Lb1.grid(row=2, column=2)

        scrollbar = Scrollbar(self)
        scrollbar.grid(row=2, column=3, sticky=N + S + W)
        Lb1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=Lb1.yview)

        back = tk.Button(self, text="Back", width=20, command=lambda: controller.show_frame("StartPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        back.grid(row=5, column=2)
        quit.grid(row=6, column=2)


class CutOffPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.sec = Cutoff("Data/cutoff.csv")
        self.jc = Cutoff("Data/jc_cutoff.csv")
        self.sec.getDict()
        self.jc.getDict()

        w1 = PanedWindow(self)
        w1.grid(row=2,column=3)
        w2 = PanedWindow(self)
        w2.grid(row=3, column=3)
        w3 = PanedWindow(self)
        w3.grid(row=3, column=5)
        #Secondary Cut Off
        L1 = tk.Label(self, text="Secondary Cut Off: ")
        L1.grid(row=1, column=1, columnspan=3)
        mini = tk.Label(self, text="Minimum: ")
        mini.grid(row=2, column=1, columnspan=2)
        E1 = Entry(w1, bd=5)
        E1.grid(row=2, column=3)
        #L2 = tk.Label(self, text="To")
        #L2.grid(row=2,column=2)
        maxi = tk.Label(self, text="Maximum: ")
        maxi.grid(row=3, column=1, columnspan=2)
        E2 = Entry(w2, bd=5)
        E2.grid(row=3, column=3, columnspan=2)
        B1 = tk.Button(self, text="Search", width=12, command=lambda: self.printInfo(E1.get(), E2.get()))
        B1.grid(row=4, column=3)
        w1.add(E1)
        w2.add(E2)
        #JC cut off
        L3 = tk.Label(self, text="JC Cut Off: ")
        L3.grid(row=1, column=5)
        variable = StringVar()
        variable.set(self.jc.getHeaders()[1])
        stream = OptionMenu(self, variable, self.jc.getHeaders()[1], self.jc.getHeaders()[2])
        stream.grid(row=2, column=5)

        E3 = Entry(w3, bd=5)
        E3.grid()
        B2 = tk.Button(self, text="Search", command=lambda: self.JCprintInfo(variable.get(), E3.get()))
        B2.grid(row=4, column=5)
        w3.add(E3)

        back = tk.Button(self, text="Back", width=20, command=lambda: controller.show_frame("StartPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        back.grid(row=9, column=4)
        quit.grid(row=10, column=4)

    def JCmessageBox(self, x):
        var = StringVar()
        label = Message(self, textvariable=var, bd=6, relief=SUNKEN)

        var.set(x)
        label.grid(row=6, column=5)

    def messageBox(self, x):
        var2 = StringVar()
        label1 = Message(self, textvariable=var2, bd=6, relief=SUNKEN)

        var2.set(x)
        label1.grid(row=6, column=2)

    def JCprintInfo(self, x, y):
        if x == "":
            tkMessageBox.showerror("Error", "Please enter input")
        else:
            info = []
            cutoff = {}
            if y.isdigit():
                info = self.jc.search(key=x, upper=y)
            if info:
                for i in range(len(info)):
                    for key, val in info[i][1][0].iteritems():
                        if key == x:
                            if val <= y:
                                print key, val
                                cutoff[info[i][0]] = val
                self.JCmessageBox(cutoff)

            else:
                tkMessageBox.showerror("Error", "Please enter input")

    def printInfo(self, x, y):
        try:
            if x == "":
                self.messageBox("")
            else:
                info = self.sec.search(lower=x, upper=y)
                self.messageBox(info)

        except:  # DO NOT USE BARE EXCEPT
            self.messageBox("No such school found!")


if __name__ == "__main__":
    app = App()
    app.minsize("1000", "500")
    app.mainloop()
