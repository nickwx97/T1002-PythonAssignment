import StringIO
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
    if writeSchTxt(s, myCSV.csvPath("School Search Info", "save")):
        tkMessageBox.showinfo("Success", "Export successful")
    else:
        tkMessageBox.showerror("Error", "Export Unsuccessful")


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
