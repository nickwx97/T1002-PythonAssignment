import readCSV


class CCA:

    def listCcaFromSch(self, key):
        result = []
        for x in self.__dict.keys():
            if key.upper() in x.upper():
                for y in self.__dict.get(x):
                    result.append(y.get("Cca_Generic_Name"))
        return result

    def searchDict(self, key="Cca_Generic_Name", value=""):
        if key not in self.__headers:
            print "Invalid search critera"
            return
        result = []
        for x in self.__dict:
            for y in self.__dict.get(x):
                for z in y:
                    if z == key:
                        if value.upper() in y.get(z).upper():
                            result.append(x)
        return result

    def getDict(self): return self.__dict

    # split into dict
    def genDict(self):
        re = readCSV.genDict(self.__raw)
        self.__headers = re[0]
        self.__dict = re[1]

    def __init__(self):
        # self.raw = readCSV.openCSV(readCSV.csvPath())
        self.__raw = readCSV.openCSV("Data/co-curricular-activities-ccas.csv")  # laziness is real, for testing purposes... :)
        self.__headers = None
        self.__dict = None


cca = CCA()
cca.genDict()
print cca.getDict()
# print cca.searchDict(value="Basketball")
# print cca.listCcaFromSch("Eunoia")
