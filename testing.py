from cutoff import *


class Debug:
    def __init__(self):
        self.jc = Cutoff("Data/jc_cutoff.csv")
        self.sec = Cutoff("Data/cutoff.csv")

    def printInfo(self):
        print self.sec.search(lower=0, upper=300)
        print self.jc.search('arts', upper=12)


db = Debug()
db.printInfo()
