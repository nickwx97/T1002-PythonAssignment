"""Reads in CSV file and performs list and dictionary manipulation for this program"""
import tkFileDialog
from Tkinter import *


class Application(Frame):
    def __fileSelect(self):
        self.__text.delete(0, END)
        self.__text.insert(0, tkFileDialog.askopenfilename())
        return

    def __fileSave(self):
        self.__text.delete(0, END)
        self.__text.insert(0, tkFileDialog.asksaveasfilename())
        return

    def __getText(self):
        self.path = self.__text.get()
        self.quit()

    def createWidgets(self, command):
        # Create quit button
        self.__NEXT["text"] = "Next"
        self.__NEXT["fg"] = "#1d7a3f"
        self.__NEXT["command"] = self.__getText
        self.__NEXT.pack({"side": "right"})

        # Create file button
        if command is 'select':
            self.__file_select["command"] = self.__fileSelect
            self.__file_select["text"] = "Select CSV File"
        elif command is 'save':
            self.__file_select["command"] = self.__fileSave
            self.__file_select["text"] = "Save CSV File"
        self.__file_select.pack({"side": "right"})

        # Create text field
        self.__text["width"] = 50
        self.__text.pack({"side": "right"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.path = ""
        # initialising widgets
        self.__file_select = Button(self)
        self.__NEXT = Button(self)
        self.__text = Entry(self)

        self.pack(expand=1)


def writeCSV(headers, data, p):
    """
    Reads in a dictionary and writes to file
    :param headers: a list containing headers for the csv
    :param data: a dictionary of data mapped by the headers
    :param p: path of file to write to
    :return: True if success, False if fail
    """
    result = ','.join(headers) + '\n'
    line = ""
    for col in data:
        newcol = None
        for x in [i for i, ltr in enumerate(col) if ltr == '"']:  # revert " to ""
            col = col[:x] + '"' + col[x:]
        if ',' in col:
            newcol = '"' + col + '"'
        for item in data.get(col):
            if newcol is None:
                line += col + ','
            else:
                line += newcol + ','
            for items in headers[1:]:
                x = item.get(items)
                if ',' in x:
                    x = '"' + x + '"'
                line += x + ','
            result += line[:-1] + '\n'
            line = ""
    try:
        csv1 = open(p, 'w')
    except IOError:
        print "Please enter valid file path!"
        return False
    else:
        csv1.writelines(result)
        csv1.close()
        return True


def csvPath(command='select'):
    """
    Creates GUI to accept user input for CSV file or to save CSV file
    :param command: command accepts 'select' or 'save', default 'select'
    :return: file path to CSV file
    """
    # Initialise GUI
    root = Tk()
    app = Application(master=root)
    if command is 'select':
        app.createWidgets('select')
    elif command is 'save':
        app.createWidgets('save')
    else:
        print "Invalid command for csvPath(), defaulting to 'select'"
        app.createWidgets('select')
    # Display GUI
    app.mainloop()
    path = app.path
    if path == "":
        print "No path specified... Quitting"
        quit(0)
    else:
        root.destroy()
        return path


def openCSV(p):
    """
    Reads in CSV file from filepath and generate multi-dimensional list
    :param p: file path
    :return: list of header and values from CSV
    """
    try:
        csv1 = open(p)
    except IOError:
        print "Please enter valid file path!"
        quit(0)
    else:
        headers = [i.lower() for i in csv1.readline().replace('\n', '').split(',')]
        content = []
        for line in csv1.readlines():
            format_line = []
            line = line.replace('\n', '').split(',')
            temp = ""
            while len(line):
                if line[0].count('"') % 2 == 1:
                    while True:
                        if temp is "":
                            temp += line.pop(0)
                        else:
                            temp += "," + line.pop(0)  # give value back it's , that we removed previously
                        if len(line) == 0:
                            break
                        if line[0].count('"') == 1:
                            temp += "," + line.pop(0)  # give value back it's , that we removed previously
                            break
                    temp = temp[1:-1].replace('""', '"')  # replace "" with " if exists, excel's way of delimiting "
                    format_line.append(temp)  # strip " from combined value
                    temp = ""
                elif line[0].count('""') >= 1:
                    format_line.append(line.pop(0)[1:-1].replace('""', '"'))
                else:
                    format_line.append(line.pop(0))
            content.append(format_line)
        csv1.close()
        return [headers, content]


def genDict(li):
    """
    Generate Dictionary from multi-dimensional list
    :param li: a multi-dimensional list of data retrieved from openCSV()
    :returns: a list with a list of headers and a dictionary of mapped values
    """
    headers = li[0]
    values = li[1]
    result = {}
    for r in values:
        if not r[0] in result.iterkeys():
            result[r[0]] = []

        temp = {}
        for c in range(1, len(headers)):
            temp[headers[c]] = r[c]
        result[r[0]].append(temp)

    return [headers, result]
