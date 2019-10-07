import Tkinter
from Tkinter import *
import tkMessageBox

import csv

class App(Tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.grid()

def search(event=None):
    sch_enquiry = school.get()
    school_dict = {}
    if sch_enquiry == "":
        tkMessageBox.showerror("Error", "Please enter a valid input")
    else:
        with open('Data/general-information-of-schools.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # schoolDict called to store information of school from csv file with the school name as the key
                school_dict[row['school_name']] = row

        # schInfoArr is the list of all the information of the requested school with the school name as the key
        sch_info_arr = list(v for k, v in school_dict.iteritems() if sch_enquiry in k.lower())
        # START test result print
        print sch_info_arr[0]
        for row in sch_info_arr:
            x = "%50s%40s" % (row['school_name'], row['address']) + "\n"
            print x
            Tkinter.Label(app, text=x).pack()

    def show_frame(self, pagename):
        frame = self.frames[pagename]
        top = Frame(self)
        bottom = Frame(self)
        top.grid()
        bottom.grid()
        frame.tkraise()

app = Tkinter.Tk()
app.minsize(1200, 400)
app.title = "GUI"

s1 = Tkinter.Label(app, text="School Name")
s1.grid(row=1, column=1)

class StartPage(Tkinter.Frame):
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
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        button1.grid(row=1, column=2)
        button2.grid(row=2, column=2)
        button3.grid(row=3, column=2)
        quit.grid(row=4, column=2)
        self.grid_columnconfigure((0, 4), weight=1)

class SearchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        var = StringVar()

        L1 = tk.Label(self, text="Name of School")
        L1.grid(row=1, column=1)
        E1 = Entry(self, bd=5)
        E1.grid(row=2, column=1)
        B1 = tk.Button(self, text="Search", command="printInfo(schstuff)")
        B1.grid(row=3, column=1)
        label1 = tk.Frame(self, borderwidth=5, relief="sunken", width=300, height=200)
        label1.grid(column=1, row=4, columnspan=3, rowspan=2, sticky=(N, S, E, W))
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
        sub1.grid(row=0,column=1)
        sub2.grid(row=0,column=2)
        sub3.grid(row=0,column=3)
        B1 = tk.Button(self, text="Search", command="")
        B1.grid(row=1,column=2)
        label1 = tk.Frame(self, borderwidth=5, relief="sunken", width=300, height=200)
        label1.grid(column=1, row=4, columnspan=3,sticky=(N, S, E, W))
        # E1 = Entry(self, bd=5)
        # E1.pack(side="top")
        back = tk.Button(self, text="Back", width=20, command=lambda: controller.show_frame("StartPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        back.grid(row=5, column=2)
        quit.grid(row=6,column=2)

        self.grid_columnconfigure((0, 7), weight=1)

class CutOffPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        var = StringVar()
        label1 = tk.Frame(self, borderwidth=5, relief="sunken", width=300, height=200)
        label1.grid(column=1, row=4, columnspan=3, sticky=(N, S, E, W))
        L1 = tk.Label(self, text="Cut Off Point: ")
        L1.grid(row=0,column=2)
        E1 = Entry(self, bd=5)
        E1.grid(row=1,column=2)
        B1 = tk.Button(self, text="Search", command="")
        B1.grid(row=2,column=2)
        label1 = tk.Frame(self, borderwidth=5, relief="sunken", width=300, height=200)
        label1.grid(column=1, row=4, columnspan=3, sticky=(N, S, E, W))
        back = tk.Button(self, text="Back", width=20, command=lambda: controller.show_frame("StartPage"))
        quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        back.grid(row=5,column=2)
        quit.grid(row=6,column=2)

if __name__ == "__main__":
    app = App()
    app.minsize("1000", "500")
    app.mainloop()
school = Tkinter.StringVar()
inputs = Tkinter.Entry(app, textvariable=school)
inputs.grid(row=1, column=2)

b1 = Tkinter.Button(app, text="Search", width=7, command=search)
b1.grid(row=1, column=3)

app.mainloop()
