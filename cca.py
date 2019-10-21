from myCSV import *


class CCA:

    def getUniqueCcaList(self):
        if self.__ccaList is not []:
            return self.genUniqueCcaList()
        else:
            return self.__ccaList

    def genUniqueCcaList(self):
        for rows in self.__dict.values():
            for cols in rows:
                if not cols.get(self.__headers[3]) in self.__ccaList:
                    self.__ccaList.append(cols.get(self.__headers[3]))
        return self.__ccaList

    def listCcaFromSch(self, key):
        result = []
        for x in self.__dict.keys():
            if key.upper() in x.upper():
                for y in self.__dict.get(x):
                    result.append(y.get("cca_generic_name"))
        return result

    def listCustomCcaFromSch(self, key):
        result = []
        for x in self.__dict.keys():
            if key.upper() in x.upper():
                for y in self.__dict.get(x):
                    if y.get("cca_customized_name").lower() == "na":
                        result.append(y.get("cca_generic_name"))
                    else:
                        result.append(y.get("cca_generic_name") + " (" + y.get("cca_customized_name")+")")
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

    def getDict(self):
        return self.__dict

    def getHeader(self):
        return self.__headers

    # split into dict
    def genDict(self):
        r = genDict(self.__raw)
        self.__headers = r[0]
        self.__dict = r[1]
        del self.__raw

    def __init__(self):
        # self.__raw = openCSV(csvPath("Select your CCA CSV"))
        self.__raw = openCSV("Data/co-curricular-activities-ccas.csv")  # lazy :)
        self.__headers = None
        self.__dict = None
        self.__ccaList = []
        self.genDict()
