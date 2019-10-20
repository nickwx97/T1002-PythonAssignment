import StringIO
import tkMessageBox
from Tkinter import *
import myCSV


def export(headers, data):
    if myCSV.writeCSV(headers, data, myCSV.csvPath("Saving Secondary cutoff points", "save")):
        showMessage(typ="success")
    else:
        showMessage(typ="error")


def JCexport(headers, data):
    if myCSV.writeCSV(headers, data, myCSV.csvPath("Saving JC cutoff points", "save")):
        showMessage(typ="success")
    else:
        showMessage(typ="error")


def schexport(x):
    s = StringIO.StringIO(x)
    path = myCSV.csvPath("School Search Info", "save", filetype="txt")
    if not path:
        showMessage(typ="error")
        return
    if writeSchTxt(s, path):
        showMessage(typ="success")
    else:
        showMessage(typ="error")


def writeSchTxt(text, p):
    try:
        csv1 = open(p, 'w')
    except IOError:
        print "Please enter valid file path!"
        return False
    else:
        for line in text:
            csv1.write(line)
        csv1.write('-' * 100 + '\n\n\n')
        csv1.close()
        return True


def showMessage(typ="error"):
    root = Tk()
    root.attributes('-topmost', 1)
    root.attributes('-topmost', 0)
    root.withdraw()
    if typ == "error":
        tkMessageBox.showerror("Title", "Export Unsuccessful")
    elif typ == "success":
        tkMessageBox.showinfo("Success", "Export successful")
    root.destroy()
