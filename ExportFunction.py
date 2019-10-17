import csv
import tkMessageBox
import StringIO
import tkFileDialog


def export(x):
    try:
        filename = tkFileDialog.asksaveasfilename(initialdir='Data/', title="Save As", defaultextension=".csv",
                                                  filetypes=(("CSV", "*.csv"), ("all files", "*.*")))
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
        filename = tkFileDialog.asksaveasfilename(initialdir='Data/', title="Save As", defaultextension=".csv",
                                                  filetypes=(("CSV", "*.csv"), ("all files", "*.*")))
        header = ["School Name", "Cut Off Points"]
        with open(filename, "wb") as csvfile:
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
            filename = tkFileDialog.asksaveasfilename(initialdir='Data/', title="Save As", defaultextension=".txt", 
                                                      filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
            s = StringIO.StringIO(x)
            with open(filename, "w") as f:
                for line in s:
                    f.write(line)
                f.write('-'*100 + '\n\n\n')
            tkMessageBox.showinfo("Success", "Export successful")
            f.close()
        else:
            filename = tkFileDialog.askopenfilename(initialdir='Data/', title="Select Existing File",
                                                    defaultextension=".txt",filetypes=(("Text Files", "*.txt"),
                                                                                       ("All Files", "*.*")))
            s = StringIO.StringIO(x)
            with open(filename, "a") as f:
                for line in s:
                    f.write(line)
                f.write('-' * 100 + '\n\n\n')
            tkMessageBox.showinfo("Success", "Export successful")
            f.close()
    except:
        tkMessageBox.showerror("Error", "Export Unsuccessful")
