from readCSV import *

class Subjects_Offered:
    def getDict(self):
        return self.__dict

    def getSubjectsBySchoolName(self,school_name):
        for i in self.__dict.keys():
            if school_name.upper() == i.upper():
                return

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
    def createDict(self):
        x = genDict(self.__raw)
        self.__dict = x[1]

    def __init__(self):
        # self.rw = openCSV(csvPath())
        self.__raw = openCSV("Data/subjects-offered.csv")
        self.__dict = None

so = Subjects_Offered()
so.createDict()
# print so.getDict()
print so.getSubjectsBySchoolName('assumption english school')