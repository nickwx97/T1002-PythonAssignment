from Tkinter import *
import Tkinter as tk
import schoolInfo
from schoolByCondition import *


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.grid()
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
        label.grid()
        tk.title = "School Portal"
        button1 = tk.Button(self, text="Search By Name", width=20, command=lambda: controller.show_frame("SearchPage"))
        button2 = tk.Button(self, text="Search By Subject", width=20,
                            command=lambda: controller.show_frame("SubjectPage"))
        button3 = tk.Button(self, text="Search By Cut Off Points", width=20,
                            command=lambda: controller.show_frame("CutOffPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        button1.grid()
        button2.grid()
        button3.grid()
        quit.grid(row=5)


class SearchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        var = StringVar()

        L1 = tk.Label(self, text="Name of School")
        L1.grid(row=1, column=2)
        E1 = Entry(self, bd=5)
        E1.grid(row=2, column=1)
        B1 = tk.Button(self, text="Search", command="printInfo(schstuff)")
        B1.grid(row=3, column=1)
        label1 = Message(self, textvariable=var, bd=6, relief=SUNKEN, width=200, padx=5, pady=5)
        label1.grid(row=4, column=1, columnspan=1, rowspan=2)
        back = tk.Button(self, text="Back", width=20, command=lambda: controller.show_frame("StartPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        quit.grid(row=6, column=1)
        back.grid(row=7, column=1)


class SubjectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        var1 = tk.IntVar()
        var2 = tk.IntVar()
        var3 = tk.IntVar()
        var = StringVar()
        label1 = Message(self, textvariable=var, bd=6, relief=SUNKEN)
        label1.grid()
        label1.place(y=80, relwidth=1, height=200)
        sub1 = tk.Checkbutton(self, text="English", variable=var1)
        sub2 = tk.Checkbutton(self, text="Math", variable=var2)
        sub3 = tk.Checkbutton(self, text="Science", variable=var3)
        sub1.grid()
        sub2.grid()
        sub3.grid()
        # E1 = Entry(self, bd=5)
        # E1.pack(side="top")
        B1 = tk.Button(self, text="Search", command="")
        B1.grid()
        back = tk.Button(self, text="Back", width=20, command=lambda: controller.show_frame("StartPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        quit.grid()
        back.grid()


class CutOffPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        var = StringVar()
        label1 = Message(self, textvariable=var, bd=6, relief=SUNKEN)
        label1.grid()
        label1.place(y=80, relwidth=1, height=200)
        L1 = tk.Label(self, text="Cut Off Point: ")
        L1.grid()
        E1 = Entry(self, bd=5)
        E1.grid()
        B1 = tk.Button(self, text="Search", command="")
        B1.grid()
        back = tk.Button(self, text="Back", width=20, command=lambda: controller.show_frame("StartPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        quit.grid()
        back.grid()


if __name__ == "__main__":
    app = App()
    app.minsize("1000", "500")
    app.mainloop()
