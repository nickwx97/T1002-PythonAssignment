import tkFileDialog
from Tkinter import *


class Application(Frame):
    def fileSelect(self):
        self.text.delete(0, END)
        self.text.insert(0, tkFileDialog.askopenfilename())
        return

    def getText(self):
        self.path = self.text.get()
        self.quit()

    def createWidgets(self):
        # Create quit button
        self.NEXT["text"] = "Next"
        self.NEXT["fg"] = "#1d7a3f"
        self.NEXT["command"] = self.getText
        self.NEXT.pack({"side": "right"})

        # Create file button
        self.file_select["text"] = "Select CSV File"
        self.file_select["command"] = self.fileSelect
        self.file_select.pack({"side": "right"})

        # Create text field
        self.text["width"] = 50
        self.text.pack({"side": "right"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.path = ""
        # initialising widgets
        self.file_select = Button(self)
        self.NEXT = Button(self)
        self.text = Entry(self)

        self.pack(expand=1)
        self.createWidgets()


def csvPath():
    # Initialise GUI
    root = Tk()
    app = Application(master=root)
    # Display GUI
    app.mainloop()
    if app.path == "":
        print "No path specified... Quitting"
        quit(0)
    else:
        return app.path


# Open CSV file return 3D list with headers and content
def openCSV(p):
    csv1 = None
    try:
        csv1 = open(p)
    except IOError:
        print "Please enter valid file path!"
        quit(0)
    else:
        headers = csv1.readline().split(',')
        content = []
        for line in csv1.readlines():
            format_line = []
            line = line.replace('\n', '').split(',')
            # START combine columns with commas as part of the value
            pointer = None
            for x in range(0, len(line)):
                if line[x].count('"') == 1:
                    if pointer is not None:
                        format_line[pointer] += "," + line[x]  # give value back it's , that we removed previously
                        format_line[pointer] = format_line[pointer].replace('"', '')  # strip " from combined value
                        pointer = None
                    else:
                        pointer = x - 1
                        format_line.append(line[x])
                else:
                    format_line.append(line[x])
            content.append(format_line)
        # END combine columns with commas as part of the value
        csv1.close()
        return [headers, content]
