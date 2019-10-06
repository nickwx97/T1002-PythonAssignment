from Tkinter import *
import Tkinter as tk
import schoolInfo
from schoolByCondition import *


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, SearchPage, SubjectPage, CutOffPage):
            pagename = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[pagename] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, pagename):
        frame = self.frames[pagename]
        top = Frame(self)
        bottom = Frame(self)
        top.pack(side=TOP)
        bottom.pack(side=BOTTOM)
        frame.tkraise()

    def quit(self):
        self.root.destroy()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="welcome", font=("Courier", 44))
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Search By Name", width=20, command=lambda: controller.show_frame("SearchPage"))
        button2 = tk.Button(self, text="Search By Subject", width=20, command=lambda: controller.show_frame("SubjectPage"))
        button3 = tk.Button(self, text="Search By Cut Off Points", width=20, command=lambda: controller.show_frame("CutOffPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        button1.pack()
        button2.pack()
        button3.pack()
        quit.pack()


class SearchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        var = StringVar()
        label1 = Message(self, textvariable=var, bd=6, relief=SUNKEN)
        label1.pack(side="top")
        label1.place(y=80, relwidth=1, height=200)
        L1 = tk.Label(self, text="Name of School")

        L1.pack(side="top")
        E1 = Entry(self, bd=5)
        E1.pack(side="top")
        B1 = tk.Button(self, text="Search", command="printInfo(schstuff)")
        B1.pack()
        back = tk.Button(self, text="Back", width=20, command=lambda: controller.show_frame("StartPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        quit.pack(side="bottom")
        back.pack(side="bottom")


class SubjectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        var = StringVar()
        label1 = Message(self, textvariable=var, bd=6, relief=SUNKEN)
        label1.pack(side="top")
        label1.place(y=80, relwidth=1, height=200)
        L1 = tk.Label(self, text="Subject: ")

        L1.pack(side="top")
        E1 = Entry(self, bd=5)
        E1.pack(side="top")
        B1 = tk.Button(self, text="Search", command="")
        B1.pack()
        back = tk.Button(self, text="Back", width=20, command=lambda: controller.show_frame("StartPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        quit.pack(side="bottom")
        back.pack(side="bottom")


class CutOffPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        var = StringVar()
        label1 = Message(self, textvariable=var, bd=6, relief=SUNKEN)
        label1.pack(side="top")
        label1.place(y=80, relwidth=1, height=200)
        L1 = tk.Label(self, text="Cut Off Point: ")

        L1.pack(side="top")
        E1 = Entry(self, bd=5)
        E1.pack(side="top")
        B1 = tk.Button(self, text="Search", command="")
        B1.pack()
        back = tk.Button(self, text="Back", width=20, command=lambda: controller.show_frame("StartPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        quit.pack(side="bottom")
        back.pack(side="bottom")


if __name__ == "__main__":
    app = App()
    app.minsize("1000", "500")
    app.mainloop()

