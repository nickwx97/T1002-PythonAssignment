import csv

from schoolByCondition import *


def subjectDict():
    from collections import defaultdict
    data = defaultdict(list)
    with open('Data/subjects-offered.csv', 'rb') as data_file:
        reader = csv.DictReader(data_file)
        for row in reader:
            data[row['School_Name']].append(row['Subject_Desc'])
    return data


class SubjectsOffered:
    def getDict(self):
        return self.__dict

    def filterMultiSubs(self, filtered, result=None):
        """
        Filter the dictionary recursively for multiple subjects
        :param filtered: Subjects to filter by
        :param result: The schools that matches the critrea of all the filters
        :return: a dictionary of schools mapped to their subject
        """
        if result is None:
            result = self.__dict
        if len(filtered) == 0:
            return result
        else:
            result2 = {}
            for i in result:
                for x in result[i]:
                    if filtered[0].upper() == x[self.__headers[1]].upper() and i not in result2:
                        result2.update({i: result.get(i)})
        return self.filterMultiSubs(filtered[1:], result2)

    def getUniqueSubjectList(self):
        """
        Returns a list of unique subjects, generates it the first time the function is called.
        :return: A list of unique subjects
        """
        if self.__subList is not []:
            return self.genUniqueSubjectList()
        else:
            return self.__subList

    def genUniqueSubjectList(self):
        """
        Generates a list of unique subjects
        :return: a list of unique subjects
        """
        for rows in self.__dict.values():
            for cols in rows:
                if not cols.get(self.__headers[1]) in self.__subList:
                    self.__subList.append(cols.get(self.__headers[1]))
        return self.__subList

    def getSubjectsBySchoolName(self, school_name):
        subjects = []
        for i in self.__dict.keys():
            if i.upper() == school_name.upper():
                for x in self.__dict[i]:
                    subjects.append(x[self.__headers[1]])
        return subjects

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

    # split into dict
    def createDict(self):
        x = genDict(self.__raw)
        self.__dict = x[1]
        self.__headers = x[0]

    def __init__(self):
        self.__subList = []
        self.__raw = openCSV("Data/subjects-offered.csv")
        self.__dict = None
        self.__headers = None
        self.createDict()
