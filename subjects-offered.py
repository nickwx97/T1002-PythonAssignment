from csv import *
from schoolByCondition import *

class SubjectsOffered:
    def getDict(self):
        return self.__dict

    def getSubjectsBySchoolName(self, school_name):
        subjects = []
        for i in self.__dict.keys():
            if i.upper() == school_name.upper():
                for x in self.__dict[i]:
                    subjects.append(x[self.__headers[1]])
        return subjects  # returns an array

    def getSchoolsBySubjectDesc(self, subject_name):
        _subj_name = subject_name.upper()
        school_arr = []
        for i in self.__dict:
            for x in self.__dict[i]:
                if _subj_name in x[self.__headers[1]].upper():
                    school_arr.append(i)
        return school_arr

    def getSubjectsByLevel(self, level):
        # gets all schools under specified level
        x = schoolstuff(level, 'mainlevel_code')
        schools_arr = []
        for y in range(len(x)):
            schools_arr.append(x[y][0])
        # stores all subjects (non-duplicated)
        subjects_arr = []
        for item in schools_arr:
            subjects_temp = self.getSubjectsBySchoolName(item)
            for i in subjects_temp:
                if i not in subjects_arr:
                    subjects_arr.append(i)
        return subjects_arr

    def getSubjectsByLevel(self, level):
        # gets all schools under specified level
        x = schoolstuff(level, 'mainlevel_code')
        schools_arr = []
        for y in range(len(x)):
            schools_arr.append(x[y][0])
        # stores all subjects (non-duplicated)
        subjects_arr = []
        for item in schools_arr:
            subjects_temp = self.getSubjectsBySchoolName(item)
            for i in subjects_temp:
                if i not in subjects_arr:
                    subjects_arr.append(i)
        return subjects_arr

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


so = SubjectsOffered()
so.createDict()
print so.getSubjectsByLevel('secondary')

