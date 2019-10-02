from readCSV import *

class Subjects_Offered:
    def getDict(self):
        return self.__dict

    def getSubjectsBySchoolName(self,school_name):
        try:
            return self.__dict[school_name.upper()]
        except:
            print 'No such school name.'

    def getSchoolsBySubjectDesc(self, subject_name):
        try:
            _subj_name = subject_name.upper()
            school_arr = []
            for i in self.__dict:
                for j in self.__dict[i]:
                    if _subj_name in j.values():
                        school_arr.append(i)
                        break
            return school_arr
        except:
            print 'No such subject.'

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

        del headers, values, self.__raw  # Free up memory

    def __init__(self):
        # self.rw = openCSV(csvPath())
        self.__raw = openCSV("Data/subjects-offered.csv")
        self.__dict = None

so = Subjects_Offered()
so.genDict()

