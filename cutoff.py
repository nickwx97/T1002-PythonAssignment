from csv import *


class Cutoff:

    def search(self, key='cutoff', lower=0, upper=300):
        result = self.__dict.copy()
        for i in result.items():
            if not i[1][0].get(key.lower()).isdigit():
                del result[i[0]]
        result = filter(lambda x: lower <= int(x[1][0].get(key.lower())) <= upper, result.items())
        return result

    def sort(self, key='cutoff', reverse=False):
        self.__dict = dict((k, v) for k, v in sorted(self.__dict.items(), key=lambda kv: kv[1][0].get(key),
                                                     reverse=reverse))

    def getHeaders(self):
        return self.__headers

    def getDict(self):
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
        self.__dict = self.getDict()


# sec = Cutoff("Data/cutoff.csv")
# print sec.search(lower=0, upper=300)
# jc = Cutoff("Data/jc_cutoff.csv")
# print jc.search('arts', upper=12)
# jc.sort(key=jc.getHeaders()[1])

