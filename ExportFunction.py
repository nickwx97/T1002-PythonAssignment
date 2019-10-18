import StringIO
import tkFileDialog
import tkMessageBox
import myCSV


def export(headers, data):
    if myCSV.writeCSV(headers, data, myCSV.csvPath("Saving Secondary cutoff points", "save")):
        tkMessageBox.showinfo("Success", "Export successful")
    else:
        tkMessageBox.showerror("Error", "Export Unsuccessful")


def JCexport(headers, data):
    if myCSV.writeCSV(headers, data, myCSV.csvPath("Saving JC cutoff points", "save")):
        tkMessageBox.showinfo("Success", "Export successful")
    else:
        tkMessageBox.showerror("Error", "Export Unsuccessful")


def schexport(x):
    s = StringIO.StringIO(x)
    if myCSV.schCSV(s, myCSV.csvPath("School Search Info", "save")):
        tkMessageBox.showinfo("Success", "Export successful")
    else:
        tkMessageBox.showerror("Error", "Export Unsuccessful")




