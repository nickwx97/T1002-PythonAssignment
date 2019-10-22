"""
Creates a CCA object to store and manipulate school CCA data
"""
from myCSV import *


class CCA:

    def getUniqueCcaList(self):
        """
        Retrieve a unique list of CCAs; If not yet generated, generates it.
        :return: a unique list of CCAs
        """
        if self.__ccaList is not []:
            return self.genUniqueCcaList()
        else:
            return self.__ccaList

    def genUniqueCcaList(self):
        """
        Generates a unique list of CCAs and stores it in the CCA object.
        :return: a unique list of CCAs
        """
        for rows in self.__dict.values():
            for cols in rows:
                if not cols.get(self.__headers[3]) in self.__ccaList:
                    self.__ccaList.append(cols.get(self.__headers[3]))
        return self.__ccaList

    def listCcaFromSch(self, key):
        """
        Takes in a String or substring of the school name and search for the CCAs offered by the school(s).
        :type key: str
        :param key: String or substring of school name
        :return: A list of generic CCAs names from the school
        """
        result = []
        for x in self.__dict.keys():
            if key.upper() in x.upper():
                for y in self.__dict.get(x):
                    result.append(y.get("cca_generic_name"))
        return result

    def listCustomCcaFromSch(self, key):
        """
        Takes in a String or substring of the school name and search for the CCAs offered by the school(s).
        :param key: String or substring of school name
        :return: A list of customised CCAs names from the school
        """
        result = []
        for x in self.__dict.keys():
            if key.upper() in x.upper():
                for y in self.__dict.get(x):
                    if y.get("cca_customized_name").lower() == "na":
                        result.append(y.get("cca_generic_name"))
                    else:
                        result.append(y.get("cca_generic_name") + " (" + y.get("cca_customized_name") + ")")
        return result

    def searchDict(self, key="cca_generic_name", value=""):
        """
        Search for a value in column defined by the user.
        :type key: str
        :type value: str
        :param key: column to search in
        :param value: value to seach in column
        :return: A list containing the schools with their respective CCAs
        """
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
        """
        Returns a dictionary with all the schools' CCAs.
        :return: A dictionary with all the schools' CCAs
        """
        return self.__dict

    def getHeader(self):
        """
        Returns the headers of which the data is mapped by.
        :return: A list of headers
        """
        return self.__headers

    def genDict(self):
        """
        Generates a dictionary mapped by the headers from the raw data taken from the CSV file and stores in the object,
        then deletes the raw data to save memory.
        """
        r = genDict(self.__raw)
        self.__headers = r[0]
        self.__dict = r[1]
        del self.__raw

    def __init__(self):
        # self.__raw = openCSV(csvPath("Select your CCA CSV"))
        self.__raw = openCSV("Data/co-curricular-activities-ccas.csv")
        self.__headers = None
        self.__dict = None
        self.__ccaList = []
        self.genDict()
