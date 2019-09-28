from readCSV import *


class CCA():
    def __init__(self):
        self.raw = openCSV(csvPath())


cca = CCA()

for i in range(len(cca.raw)):
    if i == 0:
        print cca.raw[i]
    else:
        for line in cca.raw[i]:
            print line