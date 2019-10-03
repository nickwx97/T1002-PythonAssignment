from readCSV import *


class Cutoff:

    def getSecCSV(self):
        return self.__secCSV

    def getJcCSV(self):
        return self.__jcCSV

    def __init__(self):
        # self.__jcCSV = openCSV(csvPath())
        # self.__secCSV = openCSV(csvPath())
        self.__jcCSV = openCSV("Data/jc_cutoff.csv")  # lazy
        self.__secCSV = openCSV("Data/cutoff.csv")  # lazy


co = Cutoff()
