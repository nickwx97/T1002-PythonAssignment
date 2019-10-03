import readCSV


class Cutoff:

    def getSecList(self):
        return readCSV.genDict(self.__secList)[1]

    def getJcList(self):
        return readCSV.genDict(self.__jcList)[1]

    def __init__(self):
        # self.__jcCSV = readCSV.openCSV(readCSV.csvPath())
        # self.__secCSV = readCSV.openCSV(readCSV.csvPath())
        self.__jcList = readCSV.openCSV("Data/jc_cutoff.csv")  # lazy
        self.__secList = readCSV.openCSV("Data/cutoff.csv")  # lazy


co = Cutoff()
print co.getJcList()
print co.getSecList()