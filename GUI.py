from Tkinter import *
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

        var = StringVar()
        label1 = tk.Frame(self, borderwidth=5, relief="sunken", width=300, height=200)
        label1.grid(column=1, row=4, columnspan=3, sticky=(N, S, E, W))
        L1 = tk.Label(self, text="Location: ")
        L1.grid(row=0, column=2)
        E1 = Entry(self, bd=5)
        E1.grid(row=1, column=2)
        B1 = tk.Button(self, text="Search", command="")
        B1.grid(row=2, column=2)
        label1 = tk.Frame(self, borderwidth=5, relief="sunken", width=300, height=200)
        label1.grid(column=1, row=4, columnspan=3, sticky=(N, S, E, W))
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

        #Secondary Cut Off
        L1 = tk.Label(self, text="Secondary Cut Off: ")
        L1.grid(row=1, column=2)
        E1 = Entry(self, bd=5)
        E1.grid(row=2, column=1)
        L2 = tk.Label(self, text="To")
        L2.grid(row=2,column=2)
        E2 = Entry(self, bd=5)
        E2.grid(row=2, column=3)
        B1 = tk.Button(self, text="Search", command=lambda: self.printInfo(E1.get()))
        B1.grid(row=3, column=2)

        #JC cut off
        L3 = tk.Label(self, text="JC Cut Off: ")
        L3.grid(row=1, column=15)
        variable = StringVar()
        variable.set(self.jc.getHeaders()[1])
        stream = OptionMenu(self, variable, self.jc.getHeaders()[1], self.jc.getHeaders()[2])
        stream.grid(row=2, column=14)

        E3 = Entry(self, bd=5)
        E3.grid(row=2, column=16)
        B2 = tk.Button(self, text="Search", command=lambda: self.JCprintInfo(variable.get(), E2.get()))
        B2.grid(row=2, column=17)

        back = tk.Button(self, text="Back", width=20, command=lambda: controller.show_frame("StartPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        back.grid(row=5, column=2)
        quit.grid(row=6, column=2)

    def messageBox(self, x):
        var = StringVar()
        label = Message(self, textvariable=var, bd=6, relief=SUNKEN)

        var.set(x)
        label.grid(row=4, column=2)
        #label.place(y=80, relwidth=1, height=200)

    def JCprintInfo(self, x, y):
        if x == "":
            self.messageBox("")
        else:
            info = []
            if y.isdigit():
                info = self.jc.search(key=x, upper=y)
            if info:
                self.messageBox(info)
            else:
                self.messageBox("No such school found")

    def printInfo(self, x):
        try:
            if x == "":
                self.messageBox("")
            else:
                info = self.sec.search(upper=x)
                self.messageBox(info)

        except:  # DO NOT USE BARE EXCEPT
            self.messageBox("No such school found!")



if __name__ == "__main__":
    app = App()
    app.minsize("1000", "500")
    app.mainloop()
