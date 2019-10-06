import readCSV


class Cutoff:

    def search(self, key='cutoff', lower=0, upper=300):
        result = self.__dict.copy()
        for i in result.items():
            if not i[1][0].get(key.lower()).isdigit():
                del result[i[0]]
        result = filter(lambda x: lower <= int(x[1][0].get(key.lower())) <= upper, result.items())
        return result

    def sort(self, key='cutoff', reverse=False):
        return sorted(self.__dict.items(), key=lambda kv: kv[1][0].get(key), reverse=reverse)

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


sec = Cutoff("Data/cutoff.csv")
jc = Cutoff("Data/jc_cutoff.csv")
# print sec.search()
# print jc.search('Arts', lower=16)
