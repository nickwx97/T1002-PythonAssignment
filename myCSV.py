"""Reads in CSV file and performs list and dictionary manipulation for this program"""
import tkFileDialog as tkfd
from Tkinter import *


class Application(Frame):
    def __fileSelect(self, filetype):
        temp = self.__text.get()
        self.__text.delete(0, END)
        if filetype == "csv":
            self.__text.insert(0, tkfd.askopenfilename(filetypes=[("CSV files", "*.csv")]))
        elif filetype == "txt":
            self.__text.insert(0, tkfd.askopenfilename(filetypes=[("Text files", "*.txt")]))
        else:
            print "Invalid file select option."
            self.__text.insert(0, temp)
        if not self.__text.get():
            self.__text.insert(0, temp)
        return

    def __fileSave(self, filetype):
        temp = self.__text.get()
        self.__text.delete(0, END)
        if filetype == "csv":
            self.__text.insert(0, tkfd.asksaveasfilename(filetypes=[("CSV files", "*.csv")]))
        elif filetype == "txt":
            self.__text.insert(0, tkfd.asksaveasfilename(filetypes=[("Text files", "*.txt")]))
        else:
            print "Invalid file save option."
            self.__text.insert(0, temp)
        if not self.__text.get():
            self.__text.insert(0, temp)
        elif filetype == "csv" and ".csv" not in self.__text.get():
            self.__text.insert(END, ".csv")
        elif filetype == "txt" and ".txt" not in self.__text.get():
            self.__text.insert(END, ".txt")
        return

    def __getText(self):
        self.path = self.__text.get()
        self.quit()

    def createWidgets(self, command, defText, filetype):
        # Create quit button
        self.__NEXT["text"] = "Next"
        self.__NEXT["fg"] = "#1d7a3f"
        self.__NEXT["command"] = self.__getText
        self.__NEXT.pack({"side": "right"})

        # Create file button
        if command is 'select':
            self.__file_select["command"] = lambda: self.__fileSelect(filetype)
            self.__file_select["text"] = "Select File"
        elif command is 'save':
            self.__file_select["command"] = lambda: self.__fileSave(filetype)
            self.__file_select["text"] = "Save File"
        self.__file_select.pack({"side": "right"})

        # Create text field
        self.__text["width"] = 50
        self.__text.insert(END, defText)
        self.__text.pack({"side": "right"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.path = ""
        # initialising widgets
        self.__file_select = Button(self)
        self.__NEXT = Button(self)
        self.__text = Entry(self)

        self.pack(expand=1)
        master.attributes("-topmost", True)


def writeListCSV(headers, data, p):
    """
    Reads in a list and writes to file
    :param headers: a list containing headers for the csv
    :param data: a list containing data
    :param p: path of file to write to
    :return: True if success, False if fail
    """
    result = ','.join(headers) + '\n'
    for index, col in enumerate(data, 0):
        if type(col) is not list:
            col = col.replace('"', '""')
            if '""' in col:
                result += '"' + col + '"' + ","
            else:
                result += col + ","
        else:
            for row in col:
                row = row.replace('"', '""')
                if '""' in row:
                    result += '"' + row + '"' + ","
                else:
                    result += row + ","
            result = result[:-1] + "\n"
    try:
        csv1 = open(p, 'w')
    except IOError:
        print "Please enter valid file path!"
        return False
    else:
        csv1.writelines(result[:-1])
        csv1.close()
        return True


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

        if type(data.get(col)) is str or int or chr or float:
            result += col + "," + data.get(col) + '\n'
        else:
            for item in data.get(col):
                if newcol is None:
                    line += col + ','
                else:
                    line += newcol + ','
                if type(item) is str or int or chr or float:
                    x = item
                    if ',' in x:
                        x = '"' + x + '"'
                    line += x + ','
                elif type(item) is list:
                    x = item[0]
                    if ',' in x:
                        x = '"' + x + '"'
                    line += x + ','
                else:
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


def csvPath(defText, command='select', filetype="csv"):
    """
    Creates GUI to accept user input for CSV file or to save CSV file
    :param filetype: String containing filetype to select or save
    :type defText: String
    :param defText: default text to display in text field
    :param command: command accepts 'select' or 'save', default 'select'
    :return: file path to CSV file
    """
    # Initialise GUI
    root = Tk()
    app = Application(master=root)
    if command is 'select':
        app.createWidgets('select', defText, filetype)
    elif command is 'save':
        app.createWidgets('save', defText, filetype)
    else:
        print "Invalid command for csvPath(), defaulting to 'select'"
        app.createWidgets('select', defText)
    # Display GUI
    w = 400  # width for the Tk root
    h = 30  # height for the Tk root
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate x and y coordinates
    x = (ws * 3 / 4) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    app.mainloop()
    path = app.path
    if path == "":
        pass
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
