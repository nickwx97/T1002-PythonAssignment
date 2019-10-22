"""
Creates a Cutoff object to store cutoff points for either Secondary schools or JCs
"""
from myCSV import *


class Cutoff:

    def search(self, key='cutoff', lower=0, upper=300):
        """
        Searches the data for schools that fall within the range of numbers specified, in the specified column
        :type key: str
        :type upper: int
        :type lower: int
        :param key: the column to search in, defaults to "cutoff"
        :param lower: the lower limit of the value to search for, defaults to 0
        :param upper: the upper limit of the value to search for, defaults to 300
        :return: a dictionary of schools mapped to their respective cutoff points
        """
        result = self.__dict.copy()
        for i in result.items():
            if not i[1][0].get(key.lower()).isdigit():
                del result[i[0]]
        return dict(filter(lambda x: lower <= int(x[1][0].get(key.lower())) <= upper, result.items()))

    def mySort(self, key='cutoff', reverse=False):
        """
        Sorts the dictionary by the column specified
        :type key: str
        :type reverse: bool
        :param key: column to sort by, defeaults to "cutoff"
        :param reverse: reverse sorting, True to reverse, False for default
        """
        self.__dict = dict((k, v) for k, v in sorted(self.__dict.items(), key=lambda kv: kv[1][0].get(key),
                                                     reverse=reverse))

    def getHeaders(self):
        """
        Returns a list of headers the dictionary is mapped by
        :return: a list of headers the dictionary is mapped by
        """
        return self.__headers

    def getDict(self):
        """
        Returns a dictionary of schools with their cutoff points, dictionary is generated from the raw CSV data
        the first time this function is called.
        :return: a dictionary of school cutoff points mapped by the headers
        """
        if self.__headers is None:
            self.__list = genDict(self.__list)
            self.__headers = self.__list[0]
            self.__dict = self.__list[1]
            del self.__list
            return self.__dict
        else:
            return self.__dict

    def __init__(self, filepath):
        self.__list = openCSV(filepath)
        self.__headers = None
        self.__dict = None
        self.getDict()
