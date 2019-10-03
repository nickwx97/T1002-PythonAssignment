import readCSV


class Cutoff:

    def sort(self, key='cutoff', reverse=False):
        self.__sorted = sorted(self.__dict.items(), key=lambda kv: kv[1][0].get(key), reverse=reverse)
        return self.__sorted

    def getDict(self):
        self.__list = readCSV.genDict(self.__list)
        self.__headers = self.__list[0]
        self.__dict = self.__list[1]
        del self.__list
        return self.__dict

    def __init__(self, filepath):
        self.__list = readCSV.openCSV(filepath)  # lazy
        self.__headers = None
        self.__dict = self.getDict()
        self.__sorted = None


sec = Cutoff("Data/cutoff.csv")
jc = Cutoff("Data/jc_cutoff.csv")
