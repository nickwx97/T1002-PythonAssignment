import tkFileDialog
from Tkinter import *


class Application(Frame):
    def fileSelect(self):
        self.text.delete(0, END)
        self.text.insert(0, tkFileDialog.askopenfilename())
        return

    def getText(self):
        global path
        path = self.text.get()
        self.quit()

    def createWidgets(self):
        # Create quit button
        self.NEXT["text"] = "Next"
        self.NEXT["fg"] = "#1d7a3f"
        self.NEXT["command"] = self.getText
        self.NEXT.pack({"side": "right"})

        # Create file button
        self.hi_there["text"] = "Select CSV File"
        self.hi_there["command"] = self.fileSelect
        self.hi_there.pack({"side": "right"})

        # Create text field
        self.text["width"] = 50
        self.text.pack({"side": "right"})

    def __init__(self, master=None):
        Frame.__init__(self, master)

        # initialising widgets
        self.hi_there = Button(self)
        self.NEXT = Button(self)
        self.text = Entry(self)

        self.pack(expand=1)
        self.createWidgets()

# Initialise GUI
root = Tk()
app = Application(master=root)
# Display GUI
app.mainloop()
print "Output path after app exit: " + path
# Open CSV file
csv1 = None
try:
    csv1 = open(path)
except IOError:
    print "Please enter valid file path!"
else:
    headers = csv1.readline().split(',')
    print headers
    for line in csv1.readlines():
        print line
    csv1.close()
