import csv
import tkMessageBox
import StringIO
import tkFileDialog


def closewindow(x):
    x.destroy()


def export(x, y):
    try:
        filename = tkFileDialog.asksaveasfilename(initialdir='Data/', title="Save As", defaultextension=".csv",
                                                  filetypes=(("CSV", "*.csv"), ("all files", "*.*")))
        header = ["School Name", "Cut Off Points"]
        with open(filename, "wb") as csvfile:
            w = csv.writer(csvfile, delimiter=",")
            w.writerow([h for h in header])
            for row in x.items():
                w.writerow(row)
        csvfile.close()
        closewindow(y)
        tkMessageBox.showinfo("Success", "Export successful")
    except:
        tkMessageBox.showerror("Error", "Export Unsuccessful")
        closewindow(y)


def JCexport(x, y):
    try:
        filename = tkFileDialog.asksaveasfilename(initialdir='Data/', title="Save As", defaultextension=".csv",
                                                  filetypes=(("CSV", "*.csv"), ("all files", "*.*")))
        header = ["School Name", "Cut Off Points"]
        with open(filename, "wb") as csvfile:
            w = csv.writer(csvfile, delimiter=",")
            w.writerow([h for h in header])
            for row in x.items():
                w.writerow(row)
        csvfile.close()
        closewindow(y)
        tkMessageBox.showinfo("Success", "Export successful")

    except:
        tkMessageBox.showerror("Error", "Export Unsuccessful")
        closewindow(y)


def schexport(x, y):
    header = []
    data = []
    s = StringIO.StringIO(x)
    try:
        if tkMessageBox.askyesno('Question', 'Export as new file?'):
            filename = tkFileDialog.asksaveasfilename(initialdir='Data/', title="Save As", defaultextension=".csv",
                                                      filetypes=(("CSV", "*.csv"), ("all files", "*.*")))
            for line in s:
                if line == '\n':
                    continue
                else:
                    header.append(line.split(':')[0])
                    data.append(line.split(':')[1].replace('\n', ''))
            with open(filename, "wb") as f:
                w = csv.writer(f, delimiter=",")
                w.writerow([h for h in header])
                w.writerow([d for d in data])
                f.close()
                closewindow(y)
                tkMessageBox.showinfo("Success", "Export successful")
        else:
            filename = tkFileDialog.askopenfilename(initialdir='Data/', title="Select Existing File",
                                                    defaultextension=".csv", filetypes=(("CSV", "*.csv"),
                                                                                        ("All Files", "*.*")))
            for line in s:
                if line == '\n':
                    continue
                else:
                    data.append(line.split(':')[1].replace('\n', ''))
            with open(filename, "ab+") as f:
                w = csv.writer(f, delimiter=",")
                w.writerow([d for d in data])
                f.close()
                closewindow(y)
                tkMessageBox.showinfo("Success", "Export successful")
    except:
        tkMessageBox.showerror("Error", "Export Unsuccessful")