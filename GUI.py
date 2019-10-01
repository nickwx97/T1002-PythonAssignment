import Tkinter
import tkMessageBox
import csv

def search(event=None):
    schEnquiry = school.get()
    schoolDict = {}
    if schEnquiry == "":
        tkMessageBox.showerror("Error", "Please enter a valid input")
    else:
        with open('Data/general-information-of-schools.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # schoolDict called to store information of school from csv file with the school name as the key
                schoolDict[row['school_name']] = row

        # schInfoArr is the list of all the information of the requested school with the school name as the key
        schInfoArr = list(v for k, v in schoolDict.iteritems() if schEnquiry in k.lower())
        # START test result print
        print schInfoArr[0]
        for row in schInfoArr:
            x = "%50s%40s" % (row['school_name'], row['address']) + "\n"
            print x
            Tkinter.Label(app, text=x).pack()


app = Tkinter.Tk()
app.minsize(1200, 400)
app.title = "GUI"

s1 = Tkinter.Label(app, text="School Name")
s1.grid(row=1, column=1)

school = Tkinter.StringVar()
inputs = Tkinter.Entry(app, textvariable=school)
inputs.grid(row=1, column=2)

b1 = Tkinter.Button(app, text="Search", width=7, command=search)
b1.grid(row=1, column=3)

app.mainloop()

