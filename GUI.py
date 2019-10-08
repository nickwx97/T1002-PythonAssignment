from Tkinter import *
import Tkinter as tk
from schoolInfo import *
from schoolByCondition import *


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
        var1 = tk.IntVar()
        var2 = tk.IntVar()
        var3 = tk.IntVar()
        var = StringVar()

        sub1 = tk.Checkbutton(self, text="English", variable=var1)
        sub2 = tk.Checkbutton(self, text="Math", variable=var2)
        sub3 = tk.Checkbutton(self, text="Science", variable=var3)
        sub1.grid(row=0, column=1)
        sub2.grid(row=0, column=2)
        sub3.grid(row=0, column=3)
        B1 = tk.Button(self, text="Search", command="")
        B1.grid(row=1, column=2)
        label1 = tk.Frame(self, borderwidth=5, relief="sunken", width=300, height=200)
        label1.grid(column=1, row=4, columnspan=3, sticky=(N, S, E, W))
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

        var = StringVar()
        label1 = tk.Frame(self, borderwidth=5, relief="sunken", width=300, height=200)
        label1.grid(column=1, row=4, columnspan=3, sticky=(N, S, E, W))
        L1 = tk.Label(self, text="Cut Off Point: ")
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


if __name__ == "__main__":
    app = App()
    app.minsize("1000", "500")
    app.mainloop()
