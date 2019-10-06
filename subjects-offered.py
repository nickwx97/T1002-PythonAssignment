from readCSV import *

class Subjects_Offered:
    def getDict(self):
        return self.__dict

    def getSubjectsBySchoolName(self,school_name):
        subjects = []
        for i in self.__dict.keys():
            if i.upper() == school_name.upper():
                for x in self.__dict[i]:
                    subjects.append(x[self.__headers[1]])
        return subjects


    def getSchoolsBySubjectDesc(self, subject_name):
        try:
            _subj_name = subject_name.upper()
            school_arr = []
            for i in self.__dict:
                for x in self.__dict[i]:
                   if x[self.__headers[1]].upper() == _subj_name:
                       school_arr.append(i)
            return school_arr
        except:
            print 'No such subject.'

    # split into dict
    def createDict(self):
        x = genDict(self.__raw)
        self.__dict = x[1]
        self.__headers = x[0]

    def __init__(self):
        # self.rw = openCSV(csvPath())
        self.__raw = openCSV("Data/subjects-offered.csv")
        self.__dict = None
        self.__headers = None


so = Subjects_Offered()
so.createDict()
# print so.getDict()
