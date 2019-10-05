from csv import *


class CCA:

    def listCcaFromSch(self, key):
        result = []
        for x in self.__dict.keys():
            if key.upper() in x.upper():
                for y in self.__dict.get(x):
                    result.append(y.get("cca_generic_name"))
        return result

    def searchDict(self, key="cca_generic_name", value=""):
        if key not in self.__headers:
            print "Invalid search critera"
            return
        result = []
        for x in self.__dict:
            for y in self.__dict.get(x):
                for z in y:
                    if z == key:
                        if value.upper() in y.get(z).upper():
                            result.append((x, y.get('cca_generic_name')))
        return result

    def getDict(self): return self.__dict

    def getHeader(self): return self.__headers

    # split into dict
    def genDict(self):
        r = genDict(self.__raw)
        self.__headers = r[0]
        self.__dict = r[1]
        del self.__raw

    def __init__(self):
        self.__raw = openCSV(csvPath())
        # self.__raw = openCSV("Data/co-curricular-activities-ccas.csv")  # lazy :)
        self.__headers = None
        self.__dict = None


cca = CCA()
cca.genDict()
print cca.getDict()
# writeCSV(cca.getHeader(), cca.getDict(), csvPath('save'))
# print cca.searchDict(key='cca_grouping_desc', value="phy")
# print cca.searchDict(value="Basketball")
# print cca.listCcaFromSch("Eunoia")
