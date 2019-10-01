import Tkinter
import csv


class App(Tkinter.Frame):
    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.master = master
        self.pack(anchor="w")

        Tkinter.Label(self, text="School: ").grid(row=2, column=1, sticky="w")

        self.entry = Tkinter.StringVar()
        schoolentry = Tkinter.Entry(self, textvariable=self.entry)
        schoolentry.grid(row=3, column=4, sticky="w")




root = Tkinter.Tk()
app = App(root)
root.minsize(500, 200)
root.title = "GUI"
root.mainloop()
"""        
app = Tkinter.Tk()
# to rename the title of the window
app.title("GUI")


def function():
    areaDict = {}
    with open('C:\Users\Derek\Downloads\school-directory-and-information\general-information-of-schools.csv',
              'r') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            if row['dgp_code'] == 'BEDOK':
                Bedok = row['school_name']
        print Bedok
    csvfile.close()


app_menu = Tkinter.Menu(app)
app.config(menu=app_menu)
app.geometry("600x300")
app.resizable(0, 0)

find_menu = Tkinter.Menu(app_menu)
area_menu = Tkinter.Menu(app_menu)
app_menu.add_cascade(label="Find", menu=find_menu)
find_menu.add_command(label="School", command=app.quit())

app_menu.add_cascade(label="Area", menu=area_menu)
area_menu.add_command(label="Bedok", command=function())




edit_menu = Tkinter.Menu()
# pack is used to show the object in the window
top_frame = Tkinter.Frame(app).pack()
bottom_frame = Tkinter.Frame(app).pack()

label = Tkinter.Label(app, text="Hello World!12312313131312312313").pack()

"""