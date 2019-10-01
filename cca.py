from readCSV import *


class CCA:

    def searchDict(self, key="cca_generic_name", value=""):
        if key not in self.__headers:
            print "Invalid search critera"
            return
        result = []
        for x in self.__dict:
            for y in self.__dict.get(x):
                for z in y:
                    if z == key:
                        if value.upper() in y.get(z):
                            result.append(x)
        return result

    def getDict(self): return self.__dict

    # split into dict
    def genDict(self):
        headers = self.__raw[0]
        values = self.__raw[1]
        self.__dict = {}
        for r in values:
            if not r[0] in self.__dict.iterkeys():
                self.__dict[r[0]] = []
            else:
                temp = {}
                for c in range(1, len(headers)):
                    temp[headers[c]] = r[c]
                self.__dict[r[0]].append(temp)

        self.__headers = headers
        del values, self.__raw  # Free up memory

    def __init__(self):
        # self.raw = openCSV(csvPath())
        self.__raw = openCSV("Data/co-curricular-activities-ccas.csv")  # laziness is real, for testing purposes... :)
        self.__headers = None
        self.__dict = None


cca = CCA()
cca.genDict()
# print cca.getDict()
print cca.searchDict(value="Basketball")
