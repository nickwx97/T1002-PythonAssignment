from readCSV import *


class Subjects_Offered:
    def getDict(self):
        return self.__dict

    # split into dict
    def genDict(self):
        headers = self.__raw[0]
        values = self.__raw[1]
        self.__dict = {}
        print values

        del headers, values, self.__raw  # Free up memory

    def __init__(self):
        # self.rw = openCSV(csvPath())
        self.__raw = openCSV("Data/subjects-offered.csv")
        self.__dict = None


so = Subjects_Offered()
so.genDict()
print so.getDict()
