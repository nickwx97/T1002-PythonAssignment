'''
from cutoff import *


class Debug:
    def __init__(self):
        self.jc = Cutoff("Data/jc_cutoff.csv")
        self.sec = Cutoff("Data/cutoff.csv")

    def printInfo(self):
        print self.sec.search(lower=0, upper=300)
        print self.jc.search('arts', upper=12)


db = Debug()
db.printInfo()
'''

import csv
import tkMessageBox
import schoolInfo
import StringIO


def export(x):
    try:
        header = ["School Name", "Cut Off Points"]
        with open("Data/SecCutOffSearchResult.csv", "wb") as csvfile:
            w = csv.writer(csvfile, delimiter=",")
            w.writerow([h for h in header])
            for row in x.items():
                w.writerow(row)
        csvfile.close()
        tkMessageBox.showinfo("Success", "Export successful")
    except:
        tkMessageBox.showerror("Error", "Export Unsuccessful")


def JCexport(x):
    try:
        header = ["School Name", "Cut Off Points"]
        with open("Data/JCcutoffSearchResult.csv", "wb") as csvfile:
            w = csv.writer(csvfile, delimiter=",")
            w.writerow([h for h in header])
            for row in x.items():
                w.writerow(row)
        csvfile.close()
        tkMessageBox.showinfo("Success", "Export successful")
    except:
        tkMessageBox.showerror("Error", "Export Unsuccessful")


def schexport(x):
    try:
        if tkMessageBox.askyesno('Question', 'Export as new file?'):
            s = StringIO.StringIO(x)
            with open("Data/SchoolSearchResults.txt", "w") as f:
                for line in s:
                    f.write(line)
                f.write('-'*100 + '\n\n\n')
            tkMessageBox.showinfo("Success", "Export successful")
            f.close()
        else:
            s = StringIO.StringIO(x)
            with open("Data/SchoolSearchResults.txt", "a") as f:
                for line in s:
                    f.write(line)
                f.write('-' * 100 + '\n\n\n')
            tkMessageBox.showinfo("Success", "Export successful")
            f.close()
    except:
        tkMessageBox.showerror("Error", "Export Unsuccessful")